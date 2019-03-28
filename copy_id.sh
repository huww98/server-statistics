#!/bin/bash

readarray -t ips < ip.txt

user="huweiwen"

for ip in "${ips[@]}"
do
    echo To $ip;
    sshpass -fpassword ssh-copy-id ${user}@${ip}
done
