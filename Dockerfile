FROM nginx:1.23.3-alpine

RUN apk update && apk add certbot certbot-nginx && rm /etc/nginx/conf.d/default.conf

ADD ./conf-templates /etc/nginx/once-templates

ADD ./scripts /docker-entrypoint.d/

VOLUME /etc/letsencrypt
