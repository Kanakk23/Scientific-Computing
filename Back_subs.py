def solve(A, Y, n):
    X = [0] * n  
    
    X[n - 1] = Y[n - 1] / A[n - 1][n - 1]  

    for i in reversed(range(n - 1)):  
        summation = 0
        for j in range(i + 1, n):
            summation += A[i][j] * X[j]  
        
        X[i] = (Y[i] - summation) / A[i][i]  

    return X


n = int(input("Enter the order of the matrix: "))

matrix = []
print("Enter the matrix elements row-wise:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

Y = []
print("Enter the right-hand side vector elements:")
for i in range(n):
    Y.append(int(input()))

solution = solve(matrix, Y, n)

print("Solution:", solution)
