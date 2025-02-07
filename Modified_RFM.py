import pandas as pd

def f(x):
    y = 2*(x**3) - 2.5*x -5 
    return y

tol = 0.1
err = 100
a = 1
b = 2
F=f(a)
G=f(b)
w_old=(G*a-F*b)/(G-F)
data = {
    'a': [a],
    'b': [b],
    'w':[w_old],
    'err(%)': ["---"],
    'f(w)':[f(w_old)]
    
}



if f(w_old) * f(a) < 0:
    b = w_old
    
else:
    a = w_old
    


while err > tol:
    w_new =(G*a-F*b)/(G-F)
    
    err = (w_new-w_old)/w_new
    err=abs(err)*100

    
    if f(w_new) * f(a) < 0:
        b = w_new
        G=f(w_new)
        if(f(w_old)*f(w_new)>0):
            F=F/2
    else:
        a=w_new
        F=f(w_new)
        if(f(w_old)*f(w_new)>0):
            G=G/2
         
    data['a'].append(a)
    data['b'].append(b)
    data['err(%)'].append(err)
    data['w'].append(w_new)
    data['f(w)'].append(f(w_new))
    
    w_old=w_new

df = pd.DataFrame(data)
print(df)
print("Final root approximation:", w_old)