#!/usr/bin/python3

import sys, random

if __name__ == '__main__':
    with open('choices.txt') as f:
        filename = random.choice(f.readlines()).strip()
    with open(filename, 'rb') as f:
        content = f.read()

    buf = sys.stdout.buffer

    buf.write(b'Content-Type: image/png\n')
    buf.write(f'Content-Length: {len(content)}\n'.encode('utf-8'))
    buf.write(b'\n')
    buf.write(content)
