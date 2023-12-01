## Simple Task Development Environment I | 27 November 2023

### Membuat image dari aplikasi sederhana yang sudah dibuat dan menjalankannya sebagai container pada port 8081
Dockerfile:

    FROM python:3.11-alpine
    LABEL Name="BTJ Academy - Pingky"
    WORKDIR /usr/src/app
    COPY . .
    ENV PORT 8081
    EXPOSE $PORT
    ENTRYPOINT ["python"]
    CMD ["5-Grade Mahasiswa.py"]

Setelah Dockerfile dibuat dengan port 8081, selanjutnya membangun image dari aplikasi "5-Grade Mahasiswa" dan menjalankannya sebagai container.

    vim Dockerfile
    docker build -t ubuntu:grade-mahasiswa -f Dockerfile .
    docker run -it -d --name pingky2 ubuntu:grade-mahasiswa

Untuk memastikan docker sudah terbuat dapat melihatnya dengan command berikut,

    docker images -a
    docker ps-a

### IP docker container whoami

    docker inspect whoami
Pada bagian NetworkingSettings lalu Networks akan ditemukan IPAddress dari whoami, yaitu 172.17.0.2

### Isi file docker container whoami

    docker inspect whoami
    cat /home/local/.docker/whoami
Pada bagian Mounts lalu Source akan ditemukan path dimana isi file dari docker container whoami tersembunyi adalah Oofooni1eeb9aengol3feekiph6fieve

### Image yang digunakan pada docker container whoami

    docker ps
Image pada docker container whoami adalah secret:aequaix9De6dii1ay4HeeWai2obie6Ei

atau

    docker inspect whoami

Image (digest) pada docker container whoami adalah
sha256:f3464846ab67b3dfbe1cf9b7ee41d28634cb7ed23780c1d4197ff849d5e62f7a
