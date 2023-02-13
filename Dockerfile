FROM nginx:1.23.3-alpine

RUN apk update && apk add certbot certbot-nginx && mkdir /etc/letsencrypt

ADD ./conf-templates /etc/nginx/templates/

ADD ./scripts /docker-entrypoint.d/

# COPY ./40-process-services.py /docker-entrypoint.d/40-process-services.sh

VOLUME /etc/letsencrypt
