#!/usr/bin/env python
import json
import os.path

config_path='/etc/ssl-proxy/config.json'

service_config='''
server {{
  server_name {service}.mamoru.kiev.ua
  listen 80;

  location / {{
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
    service_config_path='/etc/nginx/conf.d/{}.conf'.format(service)
    if os.path.isfile(service_config_path):
      print('service already has config {}', service_config_path)
      continue
    service_setup=service_config.format(service=service)
    print(service_setup)
    with open(service_config_path, 'w') as service_conf:
      service_conf.write(service_setup)
