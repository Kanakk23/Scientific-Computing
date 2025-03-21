import numpy as np

def convert(A, n):
    A = np.array(A, dtype=float)  # Convert input to NumPy array
    L = np.zeros((n, n))  # Lower triangular matrix
    U = np.zeros((n, n))  # Upper triangular matrix
    P = np.eye(n)  # Permutation matrix for row swaps

    for k in range(n):
        # Pivoting: Find the maximum element in column k below diagonal
        max_row = np.argmax(abs(A[k:n, k])) + k
        if A[max_row, k] == 0:
            raise ValueError("Singular matrix detected, LU decomposition not possible.")

        # Swap rows if needed
        if max_row != k:
            A[[k, max_row]] = A[[max_row, k]]  # Swap in A
            P[[k, max_row]] = P[[max_row, k]]  # Swap in Permutation matrix
            if k > 0:
                L[[k, max_row], :k] = L[[max_row, k], :k]  # Swap in L

        L[k, k] = 1  # Diagonal of L is always 1
        for j in range(k, n):
            # Compute U[k, j]
            U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j])

        for i in range(k + 1, n):
            # Compute L[i, k] (Avoid division by zero)
            if U[k, k] == 0:
                raise ZeroDivisionError(f"Zero pivot encountered at U[{k}, {k}]")
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    return P, L, U

# Example matrix
A = [[1, 2, 1, 3], 
     [2, 4, 1, 5], 
     [3, 2, 1, 4], 
     [4, 1, 1, 3]]

print("Original Matrix A:")
print(np.array(A))

P, L, U = convert(A, 4)

print("\nPermutation Matrix P:")
print(P)

print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)

# Verifying LU decomposition: P @ A should equal L @ U
print("\nCheck P @ A == L @ U:")
print(np.allclose(P @ A, L @ U))
