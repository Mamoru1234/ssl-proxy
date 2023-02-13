#/usr/bin/env sh

set -eu;

if [ -d "/etc/letsencrypt/live/$SERVICE_HOST" ]
then
  echo "Certificate already exists for $SERVICE_HOST";
  exit 0;
fi

certbot --nginx -d $SERVICE_HOST -m $ACME_USER_MAIL -n --agree-tos
