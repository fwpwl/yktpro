#!/usr/bin/env bash
set -e

export DEPLOY_ROOT=$( cd "$( dirname "$0")" && pwd )
source ${DEPLOY_ROOT}/constants.env

${DEPLOY_ROOT}/rainpy ${DEPLOY_ROOT}/rain_django/py/deploy_rain_django.py rain-django $@
