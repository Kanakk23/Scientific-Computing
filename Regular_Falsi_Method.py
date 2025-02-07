import pandas as pd

def function(x):
    y = x**3 - 0.165*(x**2) + 3.993*(10**(-4))
    return y

tol = 10**-4

xl = 0
xr = 0.5
m_old =( xl*abs(function(xr)) + xr*abs(function(xl)))/(abs(function(xl))+abs(function(xr)))

data = {
    'xl': [],
    'xr': [],
    'xm':[],

    'f(m)':[]
    
}
data['xl'].append(xl)
data['xr'].append(xr)
data['xm'].append(m_old)
# data['err(%)'].append("----")
data['f(m)'].append(function(m_old))


if function(m_old) * function(xl) < 0:
    xr = m_old
else:
    xl = m_old
    


while abs(function(m_old))>tol:
    
    m_new = ( xl*abs(function(xr)) + xr*abs(function(xl)))/(abs(function(xl))+abs(function(xr)))

    data['xl'].append(xl)
    data['xr'].append(xr)
    data['xm'].append(m_new)
    data['f(m)'].append(function(m_new))
    
    
    if function(m_new) * function(xl) < 0:
        xr = m_new
    else:
        xl = m_new
         
    m_old = m_new

df = pd.DataFrame(data)
print(df)
print("Final root approximation:",m_old)
