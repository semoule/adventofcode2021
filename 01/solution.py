#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## MAIN
depthlist = []
with open(filepath) as fp:
  for line in fp:
    depthlist.append(int(line.strip()))

# part 1
lastdepth = 0
increase = 0
for i in range(0, len(depthlist)):
  if depthlist[i] > lastdepth and lastdepth != 0:
    increase += 1
  lastdepth = depthlist[i]
print(increase)

# part 2
lastdepth = 0
increase = 0
for i in range(0, len(depthlist)-2):
  window = depthlist[i] + depthlist[i+1] + depthlist[i+2]
  if window > lastdepth and lastdepth != 0:
    increase += 1
  lastdepth = window
print(increase)