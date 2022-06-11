import sys

if __name__ == "__main__":

    acc = {}
    for line in sys.stdin:
        if len(line.split("\t")) > 1:
            col1, col2, col3 = line.split("\t")
            col2 = col2[5:7]
            if col2 not in acc.keys():
                acc[col2] = 1
            else:
                acc[col2] = acc[col2] + 1

    for key in sorted(acc):
        sys.stdout.write("{}\t{}\n".format(key, acc[key]))
