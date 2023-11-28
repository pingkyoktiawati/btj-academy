# BTJ Academy
![BTJ Logo](https://bangunindo.com/backend_assets/img/Image-01.png)
## Simple Task

### Membuat image dari aplikasi sederhana yang sudah dibuat dan menjalankannya sebagai container pada port 8081
Code:

    vim Dockerfile
    git clone https://github.com/pingkyoktiawati/btj-academy.git
    docker build -t ubuntu:grade-mahasiswa -f Dockerfile .
    docker run -it -d --name pingky ubuntu:grade-mahasiswa
    docker ps -a
    docker images -a
        
Dockerfile:

    FROM python:3.11-alpine
    LABEL Name="BTJ Academy - Pingky"
    WORKDIR /usr/src/app
    COPY . .
    ENV PORT 8081
    EXPOSE $PORT
    ENTRYPOINT ["python"]
    CMD ["5-Grade Mahasiswa.py"]

### IP docker container whoami
172.17.0.2

### Isi file docker container whoami
Oofooni1eeb9aengol3feekiph6fieve

### Image yang digunakan pada docker container whoami
Image = secret:aequaix9De6dii1ay4HeeWai2obie6Ei
Image Id = f3464846ab67
