
#! /usr/bin/ python3

import sys
if __name__ == "__main__":

    for line in sys.stdin:
        a,b,c = line.split('   ')
        
        sys.stdout.write('{}\t{}\t{}\n'.format(a,b,c))
