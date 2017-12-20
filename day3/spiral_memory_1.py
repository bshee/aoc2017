#!/usr/bin/env python3

# Consider 1 as the origin (0, 0), and each number plotted away from it as (x, y). Then the distance is just
# ||x| + |y||.

n = int(input('Choose n: '))
assert(n >= 1)

# The idea here is just to assign the position of each number up to n by moving in the appropriate direction.
x = 0
y = 0
# Cardinal directions: NESW
direction = 'E'
x_length = 1
y_length = 1
for step in range(1, n):
    if direction == 'E':
        x += 1
        if x >= x_length:
            direction = 'N'
    elif direction == 'N':
        y += 1
        if y >= y_length:
            direction = 'W'
    elif direction == 'W':
        x -= 1
        if -x >= x_length:
            direction = 'S'
            x_length += 1
    elif direction == 'S':
        y -= 1
        if -y >= y_length:
            direction = 'E'
            y_length += 1
    else:
        print('Unrecognized direction {}'.format(direction))
print(x, y)
print(abs(x) + abs(y))
