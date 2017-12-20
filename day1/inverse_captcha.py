#!/usr/bin/env python3

# Consider taking from a file.
sequence = input('Input the sequence: ')
length = len(sequence)

# Would be good to sanity check sequence but ehhh.
sumDigits = 0
for index, value in enumerate(sequence):
    nextIndex = (index + 1) % length
    nextValue = sequence[nextIndex]
    if value == nextValue:
        sumDigits += int(value)

print(sumDigits)
