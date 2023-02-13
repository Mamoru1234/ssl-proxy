#/usr/bin/env sh

set -eu;

ME=$(basename $0)

if [ -z ${ACME_USER_MAIL+x} ];
then
  echo "$ME: ACME_USER_MAIL unset skip certbot enroll"
  exit 0;
fi

if [ -d "/etc/letsencrypt/live/$SERVICE_HOST" ]
then
  echo "$ME: Certificate already exists for $SERVICE_HOST";
  exit 0;
fi

certbot --nginx -d $SERVICE_HOST -m $ACME_USER_MAIL -n --agree-tos

# wait for port 
sleep 10;
