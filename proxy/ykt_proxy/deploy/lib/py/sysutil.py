#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Copyright 2013-2016 北京慕华信息科技有限公司
    
    Author: Huangsuoyuan
    Created: 16/9/27
    Description:
"""

import subprocess
import os
import tempfile
from util import green


class ExecError(Exception):
    def __init__(self, code, stdout, stderr):
        Exception.__init__(self)
        self.code = code
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        return "Code: {0}, stdout: {1}, stderr: {}".format(self.code, self.stderr, self.stdout)


def exec_cmd(cmd, in_content=None, remote=None, pipe=True, print_cmd=False):
    if print_cmd:
        print green('[' + (remote if remote else 'localhost') + '] [exec_cmd] ') + cmd

    if remote:
        # scp sh file to remote because the cmd may contain any kinds of quotes
        tmp_fd, tmp_fn = tempfile.mkdtemp('.sh')
        remote_tmp_fn = '/tmp/rain_tmpscript_' + os.path.basename(tmp_fn)
        try:
           os.write(tmp_fd, cmd)
           os.close(tmp_fd)
           exec_cmd('scp %s %s:%s' % (tmp_fn, remote, remote_tmp_fn))
        finally:
            os.unlink(tmp_fn)

    if not pipe:
        code = os.system(cmd)
        if code != 0:
            raise ExecError(code, '', '')
        return '', ''

    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE if in_content else None,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if in_content:
        p.stdin.write(in_content)
        p.stdin.close()

    stdout = p.stdout.read() if p.stdout else ''
    stderr = p.stderr.read() if p.stderr else ''
    code = p.wait()
    if code != 0:
        raise ExecError(code, stdout, stderr)

    if remote:
        # clean the remote tmp sh file
        try:
            exec_cmd("ssh %s 'rm -f %s'" % (remote, remote_tmp_fn))
        except ExecError, e:
            print 'Failed to clean remote file %s, reason:%s' % (remote, e.message)

    return stdout, stderr

