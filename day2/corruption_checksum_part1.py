#!/usr/bin/env python3

filename = input("Input the filename: ")

if not filename:
    filename = 'input'
with open(filename) as f:
    checksum = 0
    for line in f:
        row = [int(num) for num in line.split()]
        maxNum = max(row)
        minNum = min(row)
        # Extra challenge would be to determine min and max. Or just write more anyway.
        checksum += maxNum - minNum
    print(checksum)
