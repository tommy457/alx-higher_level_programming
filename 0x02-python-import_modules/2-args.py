#!/usr/bin/python3
import sys

if __name__ == '__main__':
    leng = len(sys.argv)
    if leng == 1:
        print("{} arguments.".format(0))
    elif leng == 2:
        print("{} argument:\n{}: {}".format(1, 1, sys.argv[1]))

    elif leng > 2:
        print("{} arguments:".format(leng - 1))
        for i in range(1, leng):
            print("{}: {}".format(i, sys.argv[i]))
