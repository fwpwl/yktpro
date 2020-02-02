#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Copyright 2013-2016 北京慕华信息科技有限公司
    
    Author: Huangsuoyuan
    Created: 16/9/27
    Description:
"""

import docker
import sys
from optparse import OptionParser


class Deploy:
    def __init__(self):
        self.known_services = {}

    def offer_services(self, services):
        self.known_services = services

    def deploy_service_container(self, service, repository=None, tag=None,
                                 opts=None, container=None, remote=None):
        # Starts a new container of the service

        container_opts = []
        if opts:
            container_opts = []

        container_name = container
        if repository:
            # Use specified image
            if not tag:
                tag = 'latest'
            image = '%s:%s' % (repository, tag)
        else:
            service_info = self.known_services.get(service)
            if not service_info:
                raise RuntimeError('Service "%s" is not recognized.' % service)
            image = service_info['image']
            if tag:
                image = image.split(':')[0] + ':' + tag

            container_name = service_info['container']
            if 'opts' in service_info.keys():
                container_opts = service_info['opts']

        if not container_name:
            raise RuntimeError('Container name is not specified.')

        docker.rotate_container(image, container_name, opts=container_opts, remote=remote)

    def main(self):
        usage = "usage: %prog [options] service"
        parser = OptionParser(usage)
        parser.add_option('--host', dest='host',
                          help="The host to deploy the service onto")
        parser.add_option('--image', dest='image',
                          help='The image without tag of the service')
        parser.add_option('-t', '--tag', dest='tag',
                          help="The service image tag")
        parser.add_option('--container', dest='container',
                          help="The options for running docker containter")
        (opts, args) = parser.parse_args()
        if len(args) != 1:
            parser.print_help()
            sys.exit(1)
        service = args[0]
        self.deploy_service_container(service, opts.image, opts.tag,
                                      #opts=opts.opts,
                                      container=opts.container,
                                      remote=opts.host)
