# -*- coding:utf-8 -*-
import importlib
import os

import re
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    执行位于management/commands子目录中的其它命令
    """

    def run_from_argv(self, argv):
        if len(argv) < 3:
            print u'========> 请在后面输入command名称，command位于management/commands任意子目录下'
            return

        command_name = argv[2]
        command_path = find_command(command_name)
        packagename = build_import_name(command_path)
        instance = importlib.import_module(packagename)

        # 直接运行subcommand
        command = instance.Command()
        command.run_from_argv([argv[0]] + argv[2:])


def find_command(name):
    """
    寻找可以执行的命令
    """

    def _find_name(path):
        return {path.split('/')[-1][:-3]: path}

    paths = filter_paths(list_all_pyfiles())
    commands = {}
    for path in paths:
        commands.update(_find_name(path))
    return commands[name]


def build_import_name(path):
    """
    从路径构造import需要的名字
    """
    if path.startswith('/'):
        path = path[1:-3]
    return re.sub('/', '.', path)


def list_pyfiles_in_app_folder(app_folder):
    """
    列出app目录内的所有可能的py文件
    """
    result = []
    for base, folders, files in os.walk(app_folder):
        # 过滤svn目录
        if '.svn' in base:
            continue
            # 过滤非py文件
        for filename in files:
            if not filename.endswith('.py') or filename.startswith('_'):
                continue
            result.append(os.path.join(base, filename))
    return result


def list_custom_apps(project_folder):
    apps = _find_apps()
    names = os.listdir(project_folder)
    apps = filter(lambda x: x in names, apps)
    return apps


def list_all_pyfiles():
    """
    列出可能包含命令的路径
    """

    def _build_relative_path(result, project_dir):
        """
        创建相对路径，移除项目目录
        """
        length = len(project_dir)
        return [item[length:] for item in result]

    from ykt_verify_proxy import settings
    project_directory = settings.BASE_DIR
    apps = list_custom_apps(project_directory)
    result = []
    for app in apps:
        result.extend(list_pyfiles_in_app_folder(os.path.join(project_directory, app)))

    return _build_relative_path(result, project_directory)


def _find_apps():
    try:
        from django.conf import settings
        apps = settings.INSTALLED_APPS
    except (AttributeError, EnvironmentError, ImportError):
        apps = []
    return apps


def filter_paths(paths):
    """
    只处理自定义app中management/commands目录内的命令
    """

    def _filter_path(path, apps):
        def _filter(path, appname):
            return path.startswith('/' + appname + '/management/commands/')

        return reduce(lambda x, y: x or y, [_filter(path, appname) for appname in apps])

    apps = _find_apps()
    return [path for path in paths if _filter_path(path, apps)]
