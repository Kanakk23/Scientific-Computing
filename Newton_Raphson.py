import pandas as pd
import sympy as sp

# Define the function f(x)
def f(x):
    y = 2*(x**3) - 2.5*x - 5 
    return y

# Calculate the derivative of f(x) symbolically
x = sp.symbols('x')
f_expr = 2*(x**3) - 2.5*x - 5
f_prime = sp.diff(f_expr, x)

# Define the function f_ that returns the derivative
def f_(x_val):
    return f_prime.evalf(subs={x: x_val})

x_old = 1
err = 100
tol = 0.1
data = {
    'x': [x_old],
    'f(x)': [f(x_old)],
    'err(%)': ['---']
}

# Iterative method to find the root
while err > tol:
    x_new = x_old - f(x_old) / f_(x_old)
    err = (x_new - x_old) / x_new
    err = abs(err) * 100
    data['x'].append(x_new)
    data['f(x)'].append(f(x_new))
    data['err(%)'].append(err)
    x_old = x_new

data = pd.DataFrame(data)
print('Newton-Raphson Method')
print(data)
print('Final approximated root is :', x_old)

# Save the output to a .txt file with a heading
with open('output.txt', 'w') as file:
    file.write("Newton-Raphson Method Iterations\n")
    file.write(data.to_string(index=False))
    file.write(f'\n\nFinal approximated root is: {x_old}\n')
