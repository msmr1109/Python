def selection_sort(arr, by):
    size = len(arr)
    for i in range(0, size-1):
        for  j in range(i+1, size):
            if by(arr[i], arr[j]) == -1:
                arr[i], arr[j] = arr[j], arr[i] 

def compare_by_length(a, b):
    a_len, b_len = len(a), len(b)
    if a_len < b_len:
        return 1

    return -1

def compare_by_dictionary(a, b):
    a_ord, b_ord = ord(a[0]), ord(b[0])
    if a_ord < b_ord:
        return 1

    return -1    

def open_file(fname):
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    return lines

if __name__ =="__main__":
    
    file = open_file("C:/Users/gayeongpark/code/Python/a.txt")
    selection_sort(file, compare_by_length)
    print file
    selection_sort(file, compare_by_dictionary)
    print file    

    names = ["lee", "jang", "yi", "aaaaa"]
    selection_sort(names, compare_by_length)
    print names
    selection_sort(names, compare_by_dictionary)
    print names
