#encoding:utf-8

preload_app = True
chdir = "/opt/ykt/app/ykt_proxy"
bind = "0.0.0.0:8080"
django_settings = "ykt_proxy.settings"
workers = 4
max_requests = 5000
user = "root"
group = "root"
access_log_format = "%(t)s %(p)s %(h)s \"%(r)s\" %(s)s %(L)s %(b)s \"%(f)s\" \"%(a)s\""
accesslog = "/opt/ykt/log/gunicorn_log_access.log"
errorlog = "/opt/ykt/log/gunicorn_log_error.log"
