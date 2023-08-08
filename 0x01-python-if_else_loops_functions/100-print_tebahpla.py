#!/usr/bin/python3

for i in range(26, 0, -1):
    if i % 2 == 0:
        char = chr(i + 96)
    else:
        char = chr(i + 64)
    print('{}'.format(char), end='')
