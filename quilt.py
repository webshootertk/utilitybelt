#!/bin/python
import random
import argparse

def pattern(v, h, n, t):
    blocks = []
    all_blocks = []
    d = "+"
    for h in range(0, int(h)):
        d = d + "---+"

    for i in range (1,int(n)+1):
        blocks.append(i)

    for j in range (0, int(t)):
        all_blocks += blocks

    random.shuffle(all_blocks)
    for k in range (0, 2):
        all_blocks.remove(5)

    print d
    for l in range(0,int(v)):
        line = "| "
        for m in range (0, int(h)):
            current = all_blocks.pop(len(all_blocks)-1)
            line = line + str(current) + " | "
        print line
        print d

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="patterns for disappearing nine quilt pattern")
    parser.add_argument("v", help="number of vertical quilt block")
    parser.add_argument("h", help="number of horizontal quilt blocks")
    parser.add_argument("n", help="number of quilt blocks patterns")
    parser.add_argument("t", help="times to use each block number of horizontal quilt blocks required")
    args = parser.parse_args()
 
    pattern(args.v, args.h, args.n, args.t)
    print "your welcome" 
