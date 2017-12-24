#!/usr/bin/env python3

def is_anagram(word1, word2):
  return sorted(list(word1)) == sorted(list(word2))

filename = input('Input the filename: ')

if not filename: filename = 'input'

with open(filename) as f:
    valid_count = 0
    for line in f:
        words = line.split()
        invalid = False
        for index, word1 in enumerate(words):
            if invalid: break
            for word2 in words[index + 1:]: 
                if is_anagram(word1, word2):
                    invalid = True
                    break
        if not invalid: valid_count += 1
print(valid_count)
