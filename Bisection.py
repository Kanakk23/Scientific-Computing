import pandas as pd

def function(x):
    y = x**3 - 0.165*(x**2) + 3.993*(10**(-4))
    return y

tol = 0.1
err = 100
xl = 0
xr = 0.11
m_old = (xl + xr) / 2

data = {
    'xl': [],
    'xr': [],
    'xm':[],
    'err(%)': [],
    'f(m)':[]
    
}
data['xl'].append(xl)
data['xr'].append(xr)
data['xm'].append(m_old)
data['err(%)'].append("----")
data['f(m)'].append(function(m_old))


if function(m_old) * function(xl) < 0:
    xr = m_old
else:
    xl = m_old
    


while err > tol:
    m_new = (xl + xr) / 2
    
    err = abs(((m_new - m_old) * 100) / m_new)

    data['xl'].append(xl)
    data['xr'].append(xr)
    data['xm'].append(m_new)
    data['err(%)'].append(err)
    data['f(m)'].append(function(m_new))
    
    
    if function(m_new) * function(xl) < 0:
        xr = m_new
    else:
        xl = m_new
         
    m_old = m_new

df = pd.DataFrame(data)
print(df)
print("Final root approximation:", (xl + xr) / 2)
