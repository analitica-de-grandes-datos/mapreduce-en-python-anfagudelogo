import sys

if __name__ == "__main__":

    acc = []
    for line in sys.stdin:
        if len(line.split()) > 1:
            a, b, c = line.split()
            c = int(c)
            acc.append((a, b, c))
        else:
            pass

    for col1, col2, col3 in sorted(acc, key=lambda element: (element[0], element[2])):
        sys.stdout.write("{}   {}   {}\n".format(col1, col2, col3))
