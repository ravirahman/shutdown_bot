# Shutdown Bot

Automatically shutdown machines after no ssh connection is detected for a prolonged time

By default, it polls every minute to see if there are any active ssh connections.
If there are no active ssh connections in the most recent 15 minute window,
this bot will shutdown the machine

Useful to prevent waste of cloud computing development workstations

Tested on Ubuntu 18.04.3

## Installation
```bash
sudo ./install.sh
```