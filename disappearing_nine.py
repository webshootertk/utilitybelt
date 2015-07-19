#!/bin/python
import random
import argparse

d ="+---+---+---+"
s = "| "
m = " | "
e =" |"

blocks = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def pattern(n):
    for i in range(0,n):
        random.shuffle(blocks)
        print d
        print s + blocks[0] + m + blocks[1] + m + blocks[2] + e
        print d
        print s + blocks[3] + m + blocks[4] + m + blocks[5] + e
        print d
        print s + blocks[6] + m + blocks[7] + m + blocks[8] + e
        print d
        print ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="patterns for disappearing nine quilt pattern")
    parser.add_argument("n", help="number of quilt patterens required")
    args = parser.parse_args()
 
    pattern(int(args.n))
    print "your welcome" 
