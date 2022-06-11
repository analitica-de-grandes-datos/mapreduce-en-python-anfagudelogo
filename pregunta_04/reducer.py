import sys

if __name__ == "__main__":

    def sort_tuple(tup):
        lst = len(tup)
        for i in range(0, lst):
            
            for j in range(0, lst-i-1):
                if (tup[j][1] > tup[j + 1][1]):
                    temp = tup[j]
                    tup[j]= tup[j + 1]
                    tup[j + 1]= temp
        return tup

    # acc = []
    # i = 0
    # for line in sys.stdin:
    #     if len(line.split('\t')) > 1:
    #         a,b,c = line.split('\t')
    #         b = int(b[:4]+b[5:7]+b[-2:])
    #         acc.append((a,b,c))


    acc = {}
    for line in sys.stdin:
        if len(line.split('\t')) > 1:
            a,b,c = line.split('\t')
            b = int(b[:4]+b[5:7]+b[-2:])
            c = int(c)
            if a not in acc.keys():
                acc[a] = [b,c]
            else:
                if acc[a][0] > b:
                    acc[a] = [b,c]
                else:
                    pass
    

    for a,b in acc.items():
        sys.stdout.write("{}\t{}\n".format(a, b[1]))

