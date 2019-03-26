#!/usr/bin/env bash
set -e
export DEPLOY_ROOT=$( cd "$( dirname "$0")" && pwd )
source ${DEPLOY_ROOT}/constants.env
PROJECT_ROOT=$( cd ${DEPLOY_ROOT}/.. && pwd )
IMAGE_NAME="${RAIN_DJANGO_IMAGE}"

cd ${DEPLOY_ROOT}/rain_django

docker build -f rain_django.dockerfile -t ${IMAGE_NAME} ${PROJECT_ROOT}
