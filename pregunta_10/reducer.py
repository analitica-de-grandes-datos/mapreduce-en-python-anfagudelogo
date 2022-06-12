import sys

if __name__ == "__main__":

    acc = {}
    for line in sys.stdin:
        if len(line.split("\t")) > 1:
            a, b = line.split("\t")
            b = b.replace("\n", "")
            b = b.replace("\r", "")
            a = int(a)
            for val in b.split(","):
                val = val.replace("\r\n", "")
                if val not in acc.keys():
                    acc[val] = [a]
                else:
                    acc[val] = acc[val] + [a]

    for element in acc:
        acc[element] = sorted(acc[element])
        acc[element] = [str(val) for val in acc[element]]

    for key in sorted(acc):
        sys.stdout.write("{}\t{}\n".format(key, ",".join(acc[key])))
