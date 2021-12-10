#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## MAIN
linecount = 0
bytelist = []
statlist = []
gammarate = ""
epsilonrate = ""

## part 1
# load data
with open(filepath) as fp:
  for line in fp:
    bytelist.append(line.strip())
    linecount += 1

# get data length and create stat list
for i in range(0, len(bytelist[0])):
  statlist.append(0)

# fill stats
for byte in bytelist:
  for i in range(0, len(byte)):
    if int(byte[i]) == 1:
      statlist[i] += 1

# generate gamma and epsilon rate
for i in range(0, len(statlist)):
  if statlist[i] > linecount/2:
    gammarate += "1"
    epsilonrate += "0"
  else:
    gammarate += "0"
    epsilonrate += "1"

# print result
print(int(gammarate,2)*int(epsilonrate,2))

## part 2
def get_common(mylist, index):
  zero_list = []
  one_list = []
  for item in mylist:
    if item[index] == "0":
      zero_list.append(item)
    else:
      one_list.append(item)
  if len(zero_list) > len(one_list):
    return zero_list
  else:
    return one_list

candidate_list = bytelist
index = 0
while len(candidate_list) > 1:
  candidate_list = get_common(candidate_list, index)
  index += 1
oxygen = int(candidate_list[0],2)


def get_least(mylist, index):
  zero_list = []
  one_list = []
  for item in mylist:
    if item[index] == "0":
      zero_list.append(item)
    else:
      one_list.append(item)
  if len(zero_list) > len(one_list):
    return one_list
  else:
    return zero_list

candidate_list = bytelist
index = 0
while len(candidate_list) > 1:
  candidate_list = get_least(candidate_list, index)
  index += 1
co2 = int(candidate_list[0],2)

# print result
print(oxygen * co2)