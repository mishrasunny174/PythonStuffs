#!/usr/bin/env python
import binascii
import sys

def bruteForce(array):
    out = ''
    for iter in range(256):
        for character in array:
            out += chr(ord(character)^iter)
        print("{}: {}\n".format(iter,out))
        out = ''


def decode(array):
    bruteForce(binascii.unhexlify(array))


def main():
    if(len(sys.argv)!=2):
        print("Usage: {} <encoded text>".format(sys.argv[0]))
    else:
        decode(sys.argv[1])

if __name__ == "__main__":
    main()