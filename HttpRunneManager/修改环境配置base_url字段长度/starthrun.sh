#!/bin/bash

cd /root/httprunnermanager2021/httprunnermanager_web

sudo kill -9 $(ps -ef|grep 'manage.py'|gawk '$0 !~/grep/ {print $2}' |tr -s '\n' ' ')
sleep 1

sudo nohup python3 manage.py runserver 0.0.0.0:9900 > log.out 2>&1 &
sleep 0.5

sudo nohup python3 manage.py celery -A HttpRunnerManager worker --loglevel=info > log.out 2>&1 & 
sleep 0.5

sudo nohup python3 manage.py celery beat --loglevel=info > log.out 2>&1 & 
sleep 0.5

sudo nohup  flower --port=5555 > log.out 2>&1 & 
sleep 0.5