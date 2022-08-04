#!/usr/bin/python3

import sys, random, os
from datetime import datetime
import cgi
import cgitb
cgitb.enable()

LOGGING = True

if __name__ == '__main__':
    buf = sys.stdout.buffer
    buf.write(b'Content-Type: text/html\n')
    buf.write(b'\n')

    with open('choices.txt') as f:
        filename = random.choice(f.readlines()).strip()
    if LOGGING:
        now = datetime.now().isoformat()
        with open('log.txt', 'a') as f:
            f.write('\t'.join(
                [now, filename] +
                [os.environ[d] for d in ['REMOTE_ADDR', 'HTTP_USER_AGENT']]) + '\n')
    with open(filename, 'rb') as f:
        content = f.read()

    buf.write(b'Content-Type: image/png\n')
    buf.write(f'Content-Length: {len(content)}\n'.encode('utf-8'))
    buf.write(b'\n')
    buf.write(content)
