import pandas as pd

def f(x):
    y = 2*(x**3) - 2.5*x - 5 
    return y

x1=1
x2=2
tol=0.1
err=100
data={
    'x':[x1,x2],
    'f(x)':[f(x1),f(x2)],
    'err':['---','---']
    
}
while(err>tol):
    x_new=x2-(f(x2)*(x2-x1)/(f(x2)-f(x1)))
    err=(x_new-x2)/x_new
    err=abs(err)*100
    
    data['x'].append(x_new)
    data['f(x)'].append(f(x_new))
    data['err'].append(err)
    x1=x2
    x2=x_new
    
data=pd.DataFrame(data)
print(data)
    