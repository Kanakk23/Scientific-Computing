# Applied Numerical Methods (MTH308)  

**Prof. B. V. R. Kumar, IIT Kanpur**  
**Jan ’25 – Apr ’25**

A collection of Python and MATLAB modules implementing classical and iterative numerical algorithms for root‑finding, linear systems, interpolation and integration.  

---

## 📚 Course & Project Overview  
This repository contains self‑contained scripts and functions for solving common numerical problems taught in MTH308:  
- **Nonlinear Root Finding**  
  - Bisection  
  - Regula‑Falsi (False‑Position)  
  - Newton‑Raphson  
  - Secant  
  - Fixed Point  
- **Linear Algebraic Systems**  
  - Gaussian Elimination  
  - LU Decomposition (Doolittle & Cholesky)  
  - Power Method (dominant eigenvalue/vector)  
- **Interpolation & Numerical Integration**  
  - Lagrange Polynomials  
  - Newton–Cotes (Trapezoidal, Simpson’s Rules)  
  - Gauss Quadrature  

Each module is implemented in both **Python** (with NumPy/SciPy) and **MATLAB**, allowing easy comparison and benchmarking.  

---

##📂 Repository Structure
```bash
mth308-numerical-methods/
│
├── Python/
│   ├── root_finding/              # Bisection, Regula‑Falsi, Newton, Secant, Fixed‑Point
│   ├── linear_systems/            # Gaussian elimination, LU (Doolittle & Cholesky), Power Method
│   └── interpolation_integration/  # Lagrange, Simpson’s, Newton‑Cotes, Gauss quadrature
│
├── MATLAB/
│   ├── root_finding.m
│   ├── linear_systems.m
│   └── interp_integration.m
│
├── examples/                      # Sample driver scripts and Jupyter notebooks
│   ├── solve_roots.ipynb
│   └── demo_matrix_solvers.ipynb
│
└── README.md
```
