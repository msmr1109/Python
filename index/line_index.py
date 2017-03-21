def read_lines(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()

    return lines

def add_index(lines, to): 
    f = open(to, 'w')
    len_lines = len(lines)
    for i in range(0, len_lines):
        data= "%d %s" %(i + 1, lines[i])
        f.write(data)
    f.close()

if __name__ == "__main__":
    lines = read_lines("C:/Users/gayeongpark/code/Python/a.txt")
    add_index(lines, "C:/Users/gayeongpark/code/Python/one.txt")
