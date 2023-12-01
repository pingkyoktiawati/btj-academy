# Simple Task Development Environment II 
#### 28 November 2023

- Membuat inventory dengan mendefinisikan daftar variables dan hosts
- Membuat playbook dengan task menjalankan docker container yang terdapat image, port, dan environment variables

### Membuat inventory
Membuat inventory menggunakan teks editor pada virtual machine:

    vim inventory.yaml

Isi dari file inventory adalah:

    all:
	    vars:
		    docker_tag: latest
		hosts:
			btj-academy:
				ansible_host: 10.184.0.100

Inventory merupakan kumpulan managed nodes atau sering disebut hostfile. Pada grup inventory ini di definisikan variabel dengan nama **docker_tag** yang akan digunakan untuk tag image pada docker container. Selain itu di definisikan host dengan nama **btj-academy** dengan IP **10.184.0.100**.

### Membuat playbook
Membuat playbook menggunakan teks editor pada virtual machine:

    vim playbook.yaml

Isi dari file playbook adalah:
  
    - name: Run Docker Container
	    hosts: btj-academy
        become: true
        tasks:
	        - docker_container:
		        name: pingky
		        image: "ubuntu:{{ docker_tag }}"
		        interactive: true
		        tty: true
		        exposed_ports:
			        - "6972"


Playbook merupakan manajemen konfigurasi. Playbook ini akan menjalankan docker container dengan host btj-academy. Konfigurasi ini dijalankan sebagai root (True). Modul yang digunakan adalah **docker_container** dengan nama container **pingky** dan image yang digunakan adalah **ubuntu versi terakhir**. Docker container ini dijalankan secara interaktif dengan port **6972**.

### Menjalankan playbook
Menjalankan playbook dengan command berikut:

    ansible-playbook -i inventory.yaml playbook.yaml

Setelah playbook dijalankan maka akan terbentuk docker container dengan nama **pingky**. Untuk memastikannya dapat menggunakan command berikut:

    docker ps -a
