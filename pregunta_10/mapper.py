#! /usr/bin/ python3

import sys

if __name__ == "__main__":

    for line in sys.stdin:
        a, b = line.split("\t")

        sys.stdout.write("{}\t{}\n".format(a, b))
