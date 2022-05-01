FROM nginx:1.21.6

RUN apt-get update \
    && apt-get install -y vim

WORKDIR /usr/share/nginx/html

COPY index.html index.html