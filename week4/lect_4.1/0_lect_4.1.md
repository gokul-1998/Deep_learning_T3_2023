## A quick recap on gradient descent and derivative
- ![](2023-10-14-08-20-36.png)
- we stareted with only one neuron and two weights w and b
- today we will see variants of GD algorithm
- ![](2023-10-14-08-24-04.png)
- https://www.youtube.com/playlist?list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC
(CS231n: Convolutional Neural Networks for Visual Recognition)
- ![](2023-10-14-08-25-51.png)
- ![](2023-10-14-08-26-15.png)
    - we had a simple network with weights w and b,and we were interested in learning these weights
- we wanted to find a sigmoid function, such that when we plot the function , then those two points shoulld lie on the function
- ![](2023-10-14-08-28-29.png)
- to do that we strarted with some random guess work , like w,b
- math part is that we want the loss function to be minimum
- we were using the squared error loss
- ![](2023-10-14-08-31-10.png)
- ![](2023-10-14-08-31-26.png)
- ![](2023-10-14-08-31-36.png)
- guess work
- ![](2023-10-14-08-32-31.png)
    - the above pic is of -6 to +6 , and the loss appropriately
- ![](2023-10-14-08-34-07.png)
- ![](2023-10-14-08-34-40.png)
- ![](2023-10-14-08-34-53.png)
- yellow point keeps miving on changing the weights

## module 5.2 : Learning parameters : Gradient descent
- ![](2023-10-14-08-36-09.png)
- ![](2023-10-14-08-37-05.png)
- taylor series - allows us to compute the value of a function at a point by knowing the value of the function and its derivatives at a nearby point
- ![](2023-10-14-08-38-02.png)
- why we needed tayor series?
    - we started off with some random value for the parameter(theta) and we wanted a new value of the parameter,
- ![](2023-10-14-08-39-45.png)
- u is the change we were making to the parameter, and it is a vector, it should be in the direction opposite to the gradient
- ![](2023-10-14-08-42-11.png)
- we arrived at the gradient descent update rule, that wherever we are, we just move in the direction opposite to the gradient , in a small step neta, 
- what is gradient
    - it is the partial derivative of the loss function , wrt w and then evaluate it at w=wt and b=bt
- ![](2023-10-14-08-45-51.png)
- so now we have a more principled way of moving in the (w,b) plane than our guess work algorithm
- ![](2023-10-14-08-47-40.png)
- only thing we dont know here was how to compute the gradient
- so we went ahead and computed that 
- ![](2023-10-14-08-48-27.png)
- ![](2023-10-14-08-48-39.png)
- ![](2023-10-14-08-49-06.png)
- ![](2023-10-14-08-49-22.png)
- we found out how to compute the gradient 
- we then wrote the gradient descent algo
- ![](2023-10-14-08-51-10.png)

- what were we doing,
    - at every point we were computing this gradient, and then we were moving in the opposite direction of the gradient
    - and then when we did that 
- ![](2023-10-14-09-10-43.png)
- when the curve was gentle, means flat, and when the slope became steep the movement was very fast, and again in gentle slope the movement was slow,
- what do we mean by movement
    - w=w-neta(del w)
    - if del w is small then the new w will be close to the old w
    - hence we wont move much
    - but if these del w (update) is large then we will move a lot, 
    - the parameters are controlling how much we move, these are actually the partial derivatives of the loss function wrt w and b
    - how does this connect to smooth and gentle surfaces
    - on smooth surfaces, we are moving slowly, that means delta w is small, and on steep surfaces we are moving fast, that means delta w is large
    - why should del w be large for steep surfaces
        - because we want to move fast on steep surfaces
        - we want to move fast on steep surfaces because we want to reach the minima
        - we want to move slowly on gentle surfaces because we dont want to overshoot the minima
        - https://youtu.be/gupSH0MU7vs?t=1246
    - what is the derivative,?
        - it is the change in the function by the change in the value of the parameter
        - it captures the sensitivity of the function wrt the change in   parameter
        - if i change the x, how much does the function change
        - for function x**2, if x=2, y=4, and x=2.5 y=6.25, so the change in y is 2.25, and the change in x is 0.5, so the derivative is 2.25/0.5=4.5
        - gradient is the movenment in the y direction divide by the movement in ght x direction
        - in those regions
        - ![](2023-10-14-09-23-31.png)
        - in the steep region, we have dy/dx very high
        - ![](2023-10-14-09-24-08.png)
        - when the steep decreases, the dy/dx decreases
        - ![](2023-10-14-09-24-33.png)
        - when we come to the vertex, the dy/dx is zero,
    - why is this happening,, because for a small change in x, we are getting a large change in y,and that is what derivative captures, 
    - Repurcations of this?
        - if we start off in a point where surface is very flat, then the gradients are going to be very very small ,and it means there will be very very small updates
        - and take a long time to move away from that flat surface, 
        - if we set max iterations as 1000, then  even after 1000 iterations and if we dont see any dramatic change in loss, because we are in this flat surface where the loss is more or less constant, then we will stop
    - we need to come out of these situations,
    - if the gradient get stuck in flat surface or in a gentle surface, then we need to come out of it, as it will take a lot of time, if we run it for 10000 time, ,then it might change, but it will take a lot of time, 
    - can we do something so that the movement of this gradient is not so slow in the flat surface, and not so fast in the steep surface