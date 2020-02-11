FROM python:2.7
MAINTAINER huangsuoyuan@xuetangx.com

ENV APP_NAME rain-django
ENV DEPLOY_DIR /pro_data

# 用aliyun的源替换原有的源
RUN echo "deb http://mirrors.aliyun.com/debian jessie main non-free contrib" > /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian jessie-updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian-security jessie/updates main non-free contrib" >> /etc/apt/sources.list \
    && apt-get update \
    && mkdir -p ~/.pip \
    && echo "[global]" >  ~/.pip/pip.conf \
    && echo "timeout = 6000" >> ~/.pip/pip.conf \
    && echo "index-url = http://mirrors.aliyun.com/pypi/simple/\ntrusted-host = mirrors.aliyun.com" >> ~/.pip/pip.conf \
    && echo "[install]" >> ~/.pip/pip.conf \
    && echo "use-mirrors = true" >> ~/.pip/pip.conf \
    && echo "mirrors = http://mirrors.aliyun.com/pypi/simple/" >> ~/.pip/pip.conf \
    && echo "trusted-host = mirrors.aliyun.com" >>  ~/.pip/pip.conf

COPY . ${DEPLOY_DIR}

RUN apt-get update && apt-get -y install cron && apt-get -y install rsyslog

RUN pip install -r ${DEPLOY_DIR}/requirements.txt \
    && apt-get install -y supervisor \
    && mkdir -p /var/log/supervisor \
    && cp ${DEPLOY_DIR}/deploy/rain_django/supervisord.conf /etc/supervisor/conf.d/supervisord.conf \
    && cp ${DEPLOY_DIR}/deploy/rain_django/run.sh /run.sh \
    && chmod +rx /run.sh \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

CMD ["/bin/sh", "-c", "/run.sh"]
