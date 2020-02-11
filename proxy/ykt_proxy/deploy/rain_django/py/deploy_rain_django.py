#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deploy import Deploy
import env

services = {
    'rain-django': {
        'image': env.load_env_variable('RAIN_DJANGO_IMAGE'),
        'container': 'rain-django',
        'opts': [
            '-v', 'rain-django:/rain-django',
            '-p', '80:39154'
        ]
    }
}

if __name__ == '__main__':
    deploy = Deploy()
    deploy.offer_services(services)
    deploy.main()
