#!/usr/bin/env python
import json
import os.path

config_path='/etc/ssl-proxy/config.json'

service_config='''
server {{
  server_name {service}.mamoru.kiev.ua
  listen 80;
  listen 443 ssl; # managed by Certbot

  # RSA certificate
  ssl_certificate /etc/letsencrypt/live/{service}.mamoru.kiev.ua/fullchain.pem; # managed by Certbot
  ssl_certificate_key /etc/letsencrypt/live/{service}.mamoru.kiev.ua/privkey.pem; # managed by Certbot

  include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot

  # Redirect non-https traffic to https
  if ($scheme != "https") {{
      return 301 https://$host$request_uri;
  }} # managed by Certbot

  location {{
    proxy_pass http://internal-docker.{service};
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }}
}}
'''

if not os.path.isfile(config_path):
  print('No config file')
  exit()

with open(config_path) as config_file:
  config_data = json.load(config_file)
  print('Start processing config')
  print(json.dumps(config_data, indent=2))
  for service in config_data['services']:
    service_setup=service_config.format(service=service)
    print(service_setup)
    with open('/etc/nginx/conf.d/{}.conf'.format(service), 'w') as service_conf:
      service_conf.write(service_setup)
