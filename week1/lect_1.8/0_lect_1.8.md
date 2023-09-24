### Lect 1.8 Perceptrons
![](2023-09-23-23-00-38.png)
![](2023-09-23-23-02-54.png)
- difference between perceptron and McCulloch Pitts Neuron is that
    -  perceptron can take real valued inputs and give real valued outputs, but McCulloch Pitts Neuron can only take binary inputs and give binary outputs
    - intro to numerical weights and bias, and a mechanism  for learning the weights and bias
    - algorithms for learning the weights and bias

![](2023-09-24-09-39-26.png)
- in the bottom left we can see that , theta is gone, and we have a bias term, and the bias term is negative theta
- w0x0 replaces the theta, and w0 is the bias term, x0 is always 1, so w0x0 is always w0
- w0 = -theta
![](2023-09-24-09-41-29.png)
![](2023-09-24-09-59-04.png)
![](2023-09-24-10-01-36.png)
![](2023-09-24-10-03-21.png)
- the bias theta is the entity that tells about the person, 
    - for eg, if you are a niche person, then you will have a high theta, and if you are a generalist, then you will have a low theta
    - in this case if you are a niche person, your bias will be -3, and only when the three inputs are on, you will go to the movie, and if you are a generalist, then your bias will be -1, and only when two inputs are on, you will go to the movie   
    - theta is also called prior or the bias    
- but if you are a movie buff, then you will go to the movie even if only one of the inputs is on, so you will have a bias of 1, and you will go to the movie even if only one of the inputs is on or even if none of the inputs are on you will go to the movie and in this case bias is 0
![](2023-09-24-10-07-32.png)
![](2023-09-24-10-08-08.png)
![](2023-09-24-10-08-27.png)

- so even in perceptron we are learning a line, in some points that lie in the positive  region, the line will be closer to the point, and in some points that lie in the negative region, the line will be closer to the point
![](2023-09-24-10-11-40.png)
![](2023-09-24-10-13-31.png)
![](2023-09-24-10-15-48.png)
    - error is 2 as two points are misclassified
    - w0 is the y intercept
    ![](2023-09-24-10-18-04.png)