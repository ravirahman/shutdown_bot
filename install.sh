#!/bin/bash

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Please re-run as root"
    exit
fi

set -x

echo "[1/2]: Installing shutdown_bot service"
cp shutdown_bot.service /etc/systemd/system/shutdown_bot.service
sudo chown root:root /etc/systemd/system/shutdown_bot.service
cp shutdown_bot.py /usr/bin/shutdown_bot
sudo chown root:root /usr/bin/shutdown_bot

echo "[2/2]: Configuring and starting shutdown_bot service"
systemctl start shutdown_bot
systemctl enable shutdown_bot
