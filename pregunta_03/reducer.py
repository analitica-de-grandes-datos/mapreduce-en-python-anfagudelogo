import sys

if __name__ == "__main__":

    acc = []
    i = 0
    for line in sys.stdin:
        if len(line.split('\t')) > 1:
            a,b = line.split('\t')
            b = int(b)
            acc.append((a,b))
            
            
def sort_tuple(tup):
    lst = len(tup)
    for i in range(0, lst):
         
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup

for a,b in sort_tuple(acc):
    sys.stdout.write("{}\t{}\n".format(a, b))


 
