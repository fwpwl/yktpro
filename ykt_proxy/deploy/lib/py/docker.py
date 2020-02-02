#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Copyright 2013-2016 北京慕华信息科技有限公司
    
    Author: Huangsuoyuan
    Created: 16/9/27
    Description:
"""


import sysutil
import json
import datetime

DOCKER_DAEMON_OPTS = ['-d']


def root_cmd(cmd, opts):
    return 'gosu root %s %s' % (cmd, ' '.join(opts))


def ps_ids(filters=None, remote=None):
    if not filters:
        filters = {}
    filter_opts = ' '.join(['-f %s=%s' % item for item in filters.items()])
    stdout, _ = sysutil.exec_cmd('docker ps -qa ' + filter_opts, remote=remote)
    return [line.strip() for line in stdout.splitlines()]


def images(remote=None):
    stdout, _ = sysutil.exec_cmd('docker images | awk \'NR>1{print $1":"$2}\'', remote=remote)
    # Skip the first line which the output header
    return stdout.splitlines()[0:]


def inspect(id_or_name, remote=None):
    stdout, _ = sysutil.exec_cmd('docker inspect ' + id_or_name, remote=remote)
    return json.loads(stdout)


def run(image, boot_cmd='', opts=None, remote=None, pipe=True):
    opts = opts if opts else []
    docker_run_cmd = 'docker run %s %s %s ' % (' '.join(opts), image, boot_cmd)
    return sysutil.exec_cmd(docker_run_cmd, remote=remote, pipe=pipe, print_cmd=True)[0].strip()


def start(id_or_name, remote=None):
    sysutil.exec_cmd('docker start %s' % id_or_name, remote=remote, print_cmd=True)


def stop(id_or_name, remote=None):
    sysutil.exec_cmd('docker stop %s' % id_or_name, remote=remote, print_cmd=True)


def rename(container_old_name, container_new_name, remote=None):
    sysutil.exec_cmd('docker rename %s %s' % (container_old_name, container_new_name), remote=remote, print_cmd=True)


def rotate_container(image, container_name, boot_cmd='', opts=None, remote=None):
    if image not in images(remote):
        raise RuntimeError("The image %s cannot be found on the host %s" % (image, remote))

    container_id = ps_ids({'name': container_name+'$'}, remote=remote)
    if container_id:
        stop(container_name, remote=remote)
        try:
            time_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            rename(container_name, container_name+'.'+time_str+'.del', remote=remote)
        except sysutil.ExecError, e:
            # roll back
            start(container_name, remote=remote)
            raise e

        run_opts = ['--name', container_name] + DOCKER_DAEMON_OPTS
        if opts:
            run_opts += opts
        run(image, boot_cmd=boot_cmd, opts=run_opts, remote=remote)
    else:
        run_opts = ['--name', container_name] + DOCKER_DAEMON_OPTS
        if opts:
            run_opts += opts
        run(image, boot_cmd=boot_cmd, opts=run_opts, remote=remote)


def up_container(image, container_name, boot_cmd='', opts=None, remote=None):
    if image not in images(remote):
        raise RuntimeError("The image %s cannot be found on the host %s" % (image,  remote))

    container_ids = ps_ids({'name': container_name}, remote)
    if container_ids:
        container_id = container_ids[0]
        container = inspect(container_id, remote)[0]
        start(container_id, remote)
        return container['Id']
    else:
        opts = opts if opts else []
        opts.append('--name'+container_name)
        return run(image, boot_cmd, opts, remote)


def ensure_container(image, container_name, boot_cmd='', opts=None, remote=None, rotate=False):
    if rotate:
        rotate_container(image, container_name, boot_cmd, opts, remote)
    else:
        up_container(image, container_name, boot_cmd, remote)
