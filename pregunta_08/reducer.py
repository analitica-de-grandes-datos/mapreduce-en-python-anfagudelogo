import sys

if __name__ == "__main__":

    acc_count = {}
    acc_sum = {}
    for line in sys.stdin:
        if len(line.split("\t")) > 1:
            col1, col2, col3 = line.split("\t")
            col3 = float(col3)
            if col1 not in acc_count.keys():
                acc_count[col1] = 1
            else:
                acc_count[col1] = acc_count[col1] + 1

            if col1 not in acc_sum.keys():
                acc_sum[col1] = col3
            else:
                acc_sum[col1] = acc_sum[col1] + col3

    for key in acc_count.keys():
        sys.stdout.write(
            "{}\t{}\t{}\n".format(key, acc_sum[key], acc_sum[key] / acc_count[key])
        )
