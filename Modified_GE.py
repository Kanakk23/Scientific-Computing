def convert(matrix, n, b):
    for k in range(n - 1):
        # **Partial Pivoting: Find the row with the maximum absolute pivot element**
        max_row = k
        for i in range(k + 1, n):
            if abs(matrix[i][k]) > abs(matrix[max_row][k]):
                max_row = i  # Update max_row if a larger pivot is found
        if(matrix[max_row][k]==0):
            continue
        
        # **Swap rows in both matrix and b**
        if max_row != k:  # Only swap if a different row is found
            matrix[k], matrix[max_row] = matrix[max_row], matrix[k]
            b[k], b[max_row] = b[max_row], b[k]

        # **Gaussian Elimination**
        for i in range(k + 1, n):
            m = matrix[i][k] / matrix[k][k]
            matrix[i][k] = 0  # Explicitly setting to 0 for numerical stability
            b[i] -= m * b[k]  # Update the right-hand side
            
            for j in range(k + 1, n):
                matrix[i][j] -= m * matrix[k][j]  # Eliminate lower elements
    
    return matrix, b



n=int(input("Enter size n"))
matrix = []
print("Enter the matrix elements row-wise:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(float(input()))
    matrix.append(row)
    
b = []
print("Enter the right-hand side vector elements:")
for i in range(n):
    b.append(float(input()))
    
convert(matrix,n,b)

def solve(A, Y, n):
    X = [0] * n  
    
    X[n - 1] = Y[n - 1] / A[n - 1][n - 1]  

    for i in reversed(range(n - 1)):  
        summation = 0
        for j in range(i + 1, n):
            summation += A[i][j] * X[j]  
        
        X[i] = (Y[i] - summation) / A[i][i]  

    return X
print(solve(matrix,b,n))