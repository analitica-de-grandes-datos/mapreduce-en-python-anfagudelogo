#! /usr/bin/ python3

import sys
from functools import reduce

if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    lista = []
    for line in sys.stdin:
        lista.append(line)
    
    def make_counts(acc, nxt):
        acc[nxt] = acc.get(nxt, 0) + 1
        return acc

    result_dict =reduce(
                make_counts,
                lista,
                {})

    for key,val in result_dict.items():
        key = key.replace('\n','')
        sys.stdout.write("{}\t{}\n".format(key, val))

    
