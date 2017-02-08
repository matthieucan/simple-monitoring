# Simple monitoring

This is a simple script used to monitor disk space and CPU load on a
Linux machine. There are situations when a full monitoring stack is
overkill.

If the collected metrics are above a certain threshold, it sends an
SMS to whichever Free Mobile (french mobile network provider) user you
specify, using Free's api. If you don't use Free, it is probably easy
to adapt it to your needs.

## Requirements

* python3
* psutil (Debian: python3-psutil, pip: psutil)

## Usage

```
./monitor.py --help

usage: monitor.py [-h] --free-user FREE_USER --free-pw FREE_PW --cpu CPU --ram
                  RAM --disk DISK

Simple system monitoring.

optional arguments:
  -h, --help            show this help message and exit
  --free-user FREE_USER
                        Free Mobile account number
  --free-pw FREE_PW     Free mobile API token
  --cpu CPU             Max CPU usage threshold (%)
  --ram RAM             Max memory (RAM) usage threshold (%)
  --disk DISK           Max disk usage threshold (%)
```

### Example

If 80% is your threshold above which you want to send an alert for
CPU, memory and disk:

```
./monitor.py --free-user FREE-USER --free-pw FREE-PW --cpu 80 --ram 80 --disk 80
```

To run it e.g. every hour, use crontab:

```
0 * * * * cd PATH/TO/simple-monitoring && ./monitor.py --free-user FREE-USER --free-pw FREE-PW --cpu 80 --ram 80 --disk 80
```
