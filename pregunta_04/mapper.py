#! /usr/bin/ python3

import sys

if __name__ == "__main__":

    for line in sys.stdin:
        lista = line.split(" ")
        sys.stdout.write("{},1\n".format(lista[0]))
