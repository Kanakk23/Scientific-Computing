import numpy as np
import pandas as pd

# Define the functions
def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*(y**2) - 57

# Partial derivatives (Jacobian)
def df1_dx(x, y):
    return 2*x + y

def df1_dy(x, y):
    return x

def df2_dx(x, y):
    return 3 * (y**2)

def df2_dy(x, y):
    return 1 + 6 * x * y

# Initialize variables
x_old = 1.5
y_old = 3.5
x_in = np.array([x_old, y_old]).reshape(2, 1)  # Column vector

tol = 0.0001
err = 100  # Initial error
iteration_data = []  # List to store iterations
iteration = 1

while err > tol:
    # Compute function values
    f = np.array([[f1(x_in[0, 0], x_in[1, 0])], 
                  [f2(x_in[0, 0], x_in[1, 0])]])

    # Compute Jacobian matrix
    K = np.array([[df1_dx(x_in[0, 0], x_in[1, 0]), df1_dy(x_in[0, 0], x_in[1, 0])], 
                  [df2_dx(x_in[0, 0], x_in[1, 0]), df2_dy(x_in[0, 0], x_in[1, 0])]])

    # Compute the inverse of K
    try:
        K_inv = np.linalg.inv(K)
    except np.linalg.LinAlgError:
        print("Jacobian matrix is singular, stopping iterations.")
        break

    # Compute update step
    del_x = -np.dot(K_inv, f)
    x_out = x_in + del_x

    # Compute error
    err = np.sqrt(del_x[0, 0]**2 + del_x[1, 0]**2) / np.sqrt(x_out[0, 0]**2 + x_out[1, 0]**2)

    # Store values in list for DataFrame
    iteration_data.append([
        iteration,
        round(x_in[0, 0], 6), round(x_in[1, 0], 6),
        round(K[0, 0], 6), round(K[0, 1], 6), round(K[1, 0], 6), round(K[1, 1], 6),
        round(f[0, 0], 6), round(f[1, 0], 6),
        round(del_x[0, 0], 6), round(del_x[1, 0], 6),
        round(x_out[0, 0], 6), round(x_out[1, 0], 6),
        round(err, 6)
    ])

    # Update x_in for next iteration
    x_in = x_out
    iteration += 1

# Convert iteration data to DataFrame
df_iterations = pd.DataFrame(iteration_data, columns=[
    "Iteration",
    "x_1 in", "x_2 in",
    "K_11", "K_12", "K_21", "K_22",
    "f_1", "f_2",
    "Δ x_1", "Δ x_2",
    "x_1 out", "x_2 out",
    "err"
])

# Display DataFrame in a structured format
print(df_iterations.to_string(index=False))

# Display final result
print("\nFinal Approximated Roots:")
print(f"x_1 = {x_out[0,0]:.6f}, x_2 = {x_out[1,0]:.6f}")
