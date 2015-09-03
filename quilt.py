#!/bin/python
import random
import argparse

def pattern(v, h, n, t):
    strlen = len(' %d ' % n)
    pool = range(1,n+1) * t

    # Hack to avoid 5's
    pool = pool[:4] + pool[5:]
    pool = pool[:n+3] + pool[n+4:]

    random.shuffle(pool)
    blocks = [[pool[row * h + col] for col in range(h)] for row in range(v)]

    d = "+"
    # Scan each column for width
    for _ in range(h):
        d += "-" * strlen + "+"
    print d
    for l in range(v):
        line = "|"
        for m in range(h):
            current = blocks[l][m]
            current = " %d " % current
            while len(current) < strlen:
                current += " "
            line += str(current) + "|"
        print line
        print d

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="patterns for disappearing nine quilt pattern")
    parser.add_argument("v", type=int, help="number of vertical quilt block")
    parser.add_argument("h", type=int, help="number of horizontal quilt blocks")
    parser.add_argument("n", type=int, help="number of quilt blocks patterns")
    parser.add_argument("t", type=int, help="times to use each block number of horizontal quilt blocks required")
    args = parser.parse_args()
 
    pattern(args.v, args.h, args.n, args.t)
    print "your welcome" 
