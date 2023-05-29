#!/bin/sh

echo "starting collector container"

crontab /crontab/crontab
crond -f