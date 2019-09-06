#!/usr/bin/python3

from typing import Iterable
import subprocess
import argparse
import time
from datetime import datetime, timedelta
import syslog
import warnings

def main():
    parser = argparse.ArgumentParser(description="ShutdownBot")
    parser.add_argument('--timeout', type=int, default=(60*15), help="grace period to allow no ssh connections, in seconds")
    parser.add_argument('--poll', type=int, default=(60*1), help="interval to check for active ssh connections, in seconds")
    args = parser.parse_args()
    timeout_interval = timedelta(seconds=args.timeout)
    poll_interval = timedelta(seconds=args.poll)
    last_success_time = datetime.now()
    while True:
        poll_result = subprocess.run(["ps", "ax"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True, universal_newlines=True)
        lines: Iterable[str] = poll_result.stdout.split("\n")
        found_active_ssh = False
        for line in lines:
            if "sshd" in line:
                last_success_time = datetime.now()
                found_active_ssh = True
                break
        if not found_active_ssh:
            warnings.warn("No active ssh connection found since " + last_success_time.isoformat())
        if datetime.now() - last_success_time > timeout_interval:
            warnings.warn("Shutting down -- no active ssh connetion found since " + last_success_time.isoformat())
            subprocess.call(["shutdown", "-h", "now"], text=True)  # needs to be running as root to work
        time.sleep(poll_interval.seconds)

if __name__ == "__main__":
    main()