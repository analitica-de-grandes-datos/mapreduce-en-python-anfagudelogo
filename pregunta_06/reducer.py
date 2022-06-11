import sys

if __name__ == "__main__":

    acc_max = {}
    acc_min = {}
    for line in sys.stdin:
        if len(line.split("\t")) > 1:
            col1, col2, col3 = line.split("\t")
            col3 = float(col3)
            if col1 not in acc_max.keys():
                acc_max[col1] = col3
            else:
                if acc_max[col1] > col3:
                    acc_max[col1] = acc_max[col1]
                else:
                    acc_max[col1] = col3

            if col1 not in acc_min.keys():
                acc_min[col1] = col3
            else:
                if acc_min[col1] < col3:
                    acc_min[col1] = acc_min[col1]
                else:
                    acc_min[col1] = col3

    for key in acc_max.keys():
        sys.stdout.write("{}\t{}\t{}\n".format(key, acc_max[key], acc_min[key]))
