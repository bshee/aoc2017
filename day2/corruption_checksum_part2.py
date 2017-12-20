#!/usr/bin/env python3

filename = input("Input the filename: ")
if not filename:
    filename = 'input'

with open(filename) as f:
    checksum = 0
    for line in f:
        row = [int(num) for num in line.split()]
        done = False
        for num in row:
            for num2 in row:
                if num != num2 and num2 % num == 0:
                    checksum += num2 // num
                    done = True
                    break
            if done:
                break
    print(checksum)
