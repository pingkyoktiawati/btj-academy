# Simple Task Development Environment II 
#### 28 November 2023

- Menambahkan routing dan custom port yang di lister dari example python app
- Membuat playbook dengan beberapa task, yaitu
	- Menyalin file dari local ke server btj-academy
	- Membangun docker image untuk example python app
	- Menjalankan docker container yang sudah di build

*note: pada kasus ini, file akan disalin dari sub-folder ke folder utama yang ada diserver, hal ini karena terdapat masalah pada local*

### Mempersiapkan folder dan mengunduh example python app dari repository
Membuat folder utama yaitu btj-academy-pingky (*re: server*) dan mengunduh example python app dengan command berikut:

    mkdir btj-academy-pingky
    cd btj-academy-pingky
    git clone https://github.com/rrw-bangunindo/btj-academy.git

Menjalankan playbook pada sub-folder btj-academy (*re: local*):

    cd btj-academy

### Menambahkan routing dan custom port pada python app
Mengedit menggunakan teks editor pada virtual machine:

    vim app.py

Isi dari file app yang sudah di edit adalah:
  
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
	    return 'Hello, Docker!'
    
    @app.route('/about')
    def about():
	    return 'Docker is one of the subjects at BTJ Academy'
	
	if __name__ == '__main__':
		app.run(debug=True, host='0.0.0.0', port=5070)


Di tambahkan routing yang menampilkan **"*Docker is one of the subjects at BTJ Academy*"** dan port **5070**.

### Membuat Dockerfile
Membuat Dockerfile menggunakan teks editor pada virtual machine:

    vim Dockerfile
Isi Dockerfile:

    FROM python:3.9-alpine
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD ["python", "app.py"]
Dockerfile tersebut dibuat dengan mengatur direktori di **/app**, meng-copy file dari **host ke dalam container**, dan meng-install package yang ada di file **requirements** lalu menjalankan aplikasinya.

### Membuat Inventory
Membuat inventory menggunakan teks editor pada virtual machine:

    vim inventory-app.yaml		      
Isi dari file inventory:

    all:
        hosts:
	        btj-academy:
		        ansible_host: 10.184.0.100
Inventory merupakan kumpulan managed nodes atau sering disebut hostfile. Pada grup inventory ini di definisikan host dengan nama **btj-academy** dengan IP **10.184.0.100**.

### Membuat Playbook
Membuat playbook menggunakan teks editor pada virtual machine:

    vim playbook-app.yaml		      
Isi dari file playbook:

    - name: Copy File, Build and Run Docker Container
	  hosts: btj-academy
	  become: true
	  tasks:
		  - name: copy Dockerfile
			ansible.builtin.copy:
				src: /home/pingkyoktiawaty/btj-academy-pingky/btj-academy/Dockerfile
				dest: btj-academy-pingky
				mode: '0644'
		  - name: copy app.py
		    ansible.builtin.copy:
			    src: /home/pingkyoktiawaty/btj-academy-pingky/btj-academy/app.py
				dest: btj-academy-pingky
				mode: '0644'
		  - name: copy requirements.txt
		    ansible.builtin.copy:
				src: /home/pingkyoktiawaty/btj-academy-pingky/btj-academy/requirements.txt
				dest: btj-academy-pingky
				mode: '0644'
		  - name: build docker image
		    ansible.builtin.command:
				cmd: 'docker build -t app-flask:0.1.0 btj-academy-pingky'
		  - name: run docker container
		    ansible.builtin.command:
				cmd: 'docker run -it -d --name pingky-flask -p 5070:5070 app-flask:0.1.0'
    
Playbook merupakan manajemen konfigurasi. Playbook ini akan menjalankan docker container dengan host **btj-academy**. Konfigurasi ini dijalankan sebagai **root**. Modul yang digunakan untuk menyalin file Dockerfile, app python, dan requirements adalah **ansible.builtin.copy** dengan sumber local pada sub-folder **btj-academy** dan tujuan server pada folder **btj-academy-pingky**. Mode hak aksesnya adalah **0644** atau **rw-r--r--**, artinya pemilik memiliki hak baca dan tulis (4 + 2 = 6), grup hanya memiliki hak baca (4), dan lainnya memiliki hak baca (4). Kemudian modul yang digunakan untuk membangun docker image dan menjalankan docker containernya adalah **ansible.builtin.command**. Perintah tersebut membangun image dengan nama  **app-flask:0.1.0** dan nama container **pingky-flask**. Docker container ini dijalankan pada port **5070**.

### Menjalankan Playbook
Menjalankan playbook dengan command berikut:

    ansible-playbook -i inventory-app.yaml playbook-app.yaml

Setelah playbook dijalankan maka akan terbentuk docker container dengan nama **pingky-flask**. Untuk memastikannya dapat menggunakan command berikut:

    docker ps -a

### Menjalankan Website

http://btj-academy.bangunindo.io:5070/
http://btj-academy.bangunindo.io:5070/about

Untuk mendapatkan informasi bahwa website dapat berjalan pada port 5070 dan melihat history aksesnya dapat menggunakan command berikut:

    docker logs pingky-flask
