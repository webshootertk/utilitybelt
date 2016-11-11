#!/bin/python
import random
import argparse

d ="+---+---+---+---+---+---+---+---+---+---+---+"
s = "| "
m = " | "
e =" |"
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

width = 11
length = 13
total_sqrs_needed = width * length
# print total_sqrs_needed

fabrics = [20,20,20,20,16,1,1,19,1,2,1,3,1,7,8,25,10,4]
total_sqrs_have = sum(map(int, fabrics))
# print total_sqrs_have

counter = 0
each_fabrics = []

for fab in fabrics: # len(fabrics)
    for item in range(0, fab):
        each_fabrics.append(alpha[counter])
    counter = counter + 1

# print each_fabrics
# print len(each_fabrics)

random.shuffle(each_fabrics)
count = 0

print d
for up in range(0, length):
  line = s
  for over in range(0, width):
     line = line + each_fabrics[count] + m
     count = count + 1
  print line
  print d
