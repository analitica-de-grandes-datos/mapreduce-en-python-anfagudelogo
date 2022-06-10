


import sys

if __name__ == "__main__":

    acc = {}
    for line in sys.stdin:
        key,val = line.split('\t')
        val = int(val)
        if key not in acc.keys():
            acc[key] = val
        else:
            if acc[key] < val:
                acc[key] = val
            else:
                pass
    
    for key,val in acc.items():
        sys.stdout.write("{}\t{}\n".format(key, val))

 

