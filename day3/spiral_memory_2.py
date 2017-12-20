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
# Keep track of the grid with a dictionary, indexed by the x-y coordinates.
grid = {}


def sum_adjacent(grid, x, y):
    def get(x1, y1):
        return grid.get((x1, y1), 0)
    sum = get(x + 1, y)
    sum += get(x + 1, y + 1)
    sum += get(x + 1, y - 1)
    sum += get(x - 1, y)
    sum += get(x - 1, y + 1)
    sum += get(x - 1, y - 1)
    sum += get(x, y + 1)
    sum += get(x, y - 1)
    return sum

grid[(x, y)] = 1
while True:
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
    sum = sum_adjacent(grid, x, y)
    grid[(x, y)] = sum
    if sum > n: break

print(grid[(x, y)])
