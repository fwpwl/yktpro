#!/bin/bash

#source /home/ec2-user/changping/pro_data/deploy/constants.env
source /home/bl_deploy/changping/proxy/ykt_proxy/deploy/constants.env
# push to registry
docker push ${RAIN_DJANGO_IMAGE}

#ssh import_data_djangoa -C "sudo docker pull ${RAIN_DJANGO_IMAGE}"
