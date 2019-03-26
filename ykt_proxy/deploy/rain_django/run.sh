#!/usr/bin/env bash

WORK_DIR="/pro_data"
CONFIG_DIR="/rain-django"

cd ${CONFIG_DIR}

if [ -f local_settings.py ]; then
    cp local_settings.py ${WORK_DIR}/pro_data/local_settings.py
fi

if [ -f gunicorn.py ]; then
    cp gunicorn.py ${WORK_DIR}/gunicorn.py
fi

if [ -f gunicorn_supervisord.conf ]; then
    cp gunicorn_supervisord.conf /etc/supervisor/conf.d/supervisord.conf
fi

if [ -f cron ]; then
    cp -f cron /etc/pam.d/
fi


cd ${WORK_DIR}
cp -f ${WORK_DIR}/conf/cron/professional_rw /etc/crontab
rm -rf /tmp/supervisord.pid

/etc/init.d/cron start
/usr/local/bin/supervisord
