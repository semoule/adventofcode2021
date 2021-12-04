#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## MAIN
movelist = []
with open(filepath) as fp:
  for line in fp:
    movelist.append((line.split()[0],int(line.split()[1])))

# part 1
x = 0
y = 0
for move in movelist:
  if move[0] == "forward":
    x = x + move[1]
  elif move[0] == "up":
    y = y - move[1]
  elif move[0] == "down":
    y = y + move[1]
  else:
    print("error")
print(x*y)

# part 2
x = 0
y = 0
aim = 0
for move in movelist:
  if move[0] == "forward":
    x = x + move[1]
    y = y + aim * move[1]
  elif move[0] == "up":
    aim = aim - move[1]
  elif move[0] == "down":
    aim = aim + move[1]
  else:
    print("error")
print(x*y)