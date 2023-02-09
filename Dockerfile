FROM nginx:1.23.3-alpine

RUN apk update && apk add certbot certbot-nginx

RUN mkdir /etc/letsencrypt

COPY ./default.conf /etc/nginx/conf.d/default.conf
