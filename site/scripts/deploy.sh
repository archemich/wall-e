#!/usr/bin/env bash

mvn clean package

echo 'Copying files...'

scp -P 48522 -i ~/.ssh/id_rsa target/SpringPractice-1.0.jar \
  drelagreen@46.147.240.156:/home/drelagreen/

echo 'Restarting server'

ssh -i ~/.ssh/id_rsa -p 48522 drelagreen@46.147.240.156 << EOF
pgrep java | xargs kill -9
nohup java -jar SpringPractice-1.0.jar > log.txt &
EOF

echo 'Bye'