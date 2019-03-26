#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import local, hosts


@hosts("localhost")
def d():
    build_django_images()
    offer_django()


@hosts("localhost")
def build_django_images():
    local('cd /home/ec2-user/changping/pro_data/deploy && sudo ./build_rain_django.sh')


@hosts("localhost")
def offer_django():
    local('sudo sh /home/ec2-user/changping/offer_django.sh')
