import numpy as np
X=[0.5,2.5]
Y=[0.2,0.9]

def f(x,w,b):
    return 1.0/(1.0+np.exp(-(w*x+b)))

def grad_b(x,w,b,y):
    fx=f(x,w,b)
    return (fx-y)*fx*(1-fx)

def grad_w(x,w,b,y):
    fx=f(x,w,b)
    return (fx-y)*fx*(1-fx)*x

def do_gradient_descent():
    
    w,b,eta,max_epoch=-2,-2,1.0,1000

    for i in range(max_epoch):
        dw,db=0,0 # initialize derivatives to zero
        for x,y in zip(X,Y): # in data points
            dw+=grad_w(x,w,b,y) # we will compute the gradient or partial derivative for each data point w.r.t w
            db+=grad_b(x,w,b,y) # we will compute the gradient or partial derivative for each data point w.r.t b

        w=w-eta*dw # update w
        b=b-eta*db # update b