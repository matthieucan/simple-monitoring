#!/usr/bin/env python3

import argparse
import psutil
import socket
import urllib.error
import urllib.parse
import urllib.request

def send_message(user, pw, result):
    hostname = socket.getfqdn()

    message = 'Warning: ' + hostname + '\n' + '\n'.join(result)

    params = {'user': user, 'pass': pw, 'msg': message}
    params_encoded = urllib.parse.urlencode(params)

    url = 'https://smsapi.free-mobile.fr/sendmsg'

    try:
        http_res = urllib.request.urlopen(url + '?' + params_encoded)
    except urllib.error.HTTPError as e:
        raise e

    code = http_res.getcode()
    if code != 200:
        raise Exception("Couldn't send message, received {} from server".format(code))

def main():
    parser = argparse.ArgumentParser(description='Simple system monitoring.')
    parser.add_argument('--free-user', required=True,
                        help='Free Mobile account number')
    parser.add_argument('--free-pw', required=True,
                        help='Free Mobile API token')
    parser.add_argument('--cpu', required=True, type=float,
                        help='Max CPU usage threshold (%%)')
    parser.add_argument('--ram', required=True, type=float,
                        help='Max memory (RAM) usage threshold (%%)')
    parser.add_argument('--disk', required=True, type=float,
                        help='Max disk usage threshold (%%)')

    args = parser.parse_args()

    checks = [
        {'name': 'CPU usage', 'value': psutil.cpu_percent(interval=3), 'threshold': args.cpu},
        {'name': 'Memory usage', 'value': psutil.virtual_memory().percent, 'threshold': args.ram},
        {'name': 'Disk usage', 'value': psutil.disk_usage('/').percent, 'threshold': args.disk}
    ]

    result = []
    for check in checks:
        if check['value'] > check['threshold']:
            result.append('{} is at {}%%.'.format(check['name'], check['value']))

    if result:
        send_message(args.free_user, args.free_pw, result)

if __name__ == '__main__':
    main()
