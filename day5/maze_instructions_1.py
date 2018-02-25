#!/usr/bin/env python3

filename = input('Input the filename: ')

if not filename: filename = 'input'

# The number of instructions that need to be followed to exit the maze.
steps = 0
program_counter = 0
with open(filename) as f:
  # Store the list of instructions on each line as a List.
  instructions = [int(instruction) for instruction in f.readlines()]
  num_instructions = len(instructions)

  # Determine if the CPU has exited.
  def exited_maze():
    return program_counter < 0 or program_counter >= num_instructions

  # Assume each list of instructions does contain a way to exit.
  while True:
    offset = instructions[program_counter]
    instructions[program_counter] += 1
    program_counter += offset
    steps += 1
    if exited_maze(): break

print(steps)
