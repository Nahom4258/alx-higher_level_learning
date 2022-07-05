#!/usr/bin/python3
for char in range(26):
    if chr(char) != 'e' and chr(char) != 'q':
        print("{:s}".format(chr(char + ord("a"))), end="")
