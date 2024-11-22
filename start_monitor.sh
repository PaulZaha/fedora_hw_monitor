#!/bin/bash

cd "/mnt/Z/Repositories/fedora_hw_monitor/src/frontend" || exit
gnome-terminal -- bash -c "npm run dev; exec bash"

cd "/mnt/Z/Repositories/fedora_hw_monitor/environment" || exit
source bin/activate

cd "/mnt/Z/Repositories/fedora_hw_monitor/src/backend" || exit
gnome-terminal -- bash -c "python backend_server.py; exec bash"

