def find_coeffcient(n):
    a = [[0]*(n+1)]*(n+1)
    a[0][n] = 1
    for i in range(1, n + 1):
        for j in range(0, n):
            a[i][j] = a[i-1][j] + a[i-1][j+1]
        
    return a[n]
if __name__ == "__main__":
    print(find_coeffcient(2))  
    print(find_coeffcient(3))  
    print(find_coeffcient(10))  

