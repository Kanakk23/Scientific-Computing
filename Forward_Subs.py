def solve(A, Y, n):
    X = []
    x = Y[0] / A[0][0]
    X.append(x)
    
    for i in range(1, n):
        sum = 0
        for j in range(0, i):
            sum += A[i][j] * X[j]
        
        x = (Y[i] - sum) / A[i][i]
        X.append(x)
    
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
