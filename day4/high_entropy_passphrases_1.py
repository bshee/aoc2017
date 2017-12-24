#!/usr/bin/env python3

filename = input('Input the filename: ')

if not filename: filename = 'input'

with open(filename) as f:
  valid_count = 0
  for line in f:
    words = line.split()
    distinct_words = set(words)
    if len(words) == len(distinct_words): valid_count += 1
print(valid_count)
