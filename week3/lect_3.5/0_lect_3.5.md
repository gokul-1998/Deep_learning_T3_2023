## 3.5 Backpropagation Computing : Gradient w.r.t output units

- ![](2023-10-09-19-11-09.png)
- we will slowly talk to all the stake holders of gradient computation
    - output layer
    - hidden layer
    - weights
- start with first, Talk to output layers
- we want to compute the derivative of the loss function, with r.t the output units
- it has two parts, 
    - activation 
    - pre-activation
- ![](2023-10-09-19-13-25.png)
- we know that it would be collection of some partial derivatives
- ![](2023-10-09-19-14-13.png)
- we will do it on the first half of the upper layer
- ![](2023-10-09-19-15-22.png)
- we are trying to take derivative of the loss function , which has the term yhatl, with restpect to one of y hats   , this depends only on one of the elements in the array, the one which corresponds to the true loss fiunctino
- ![](2023-10-09-19-19-24.png)
- here since  y2 is responsible , others are not responsible, so we will have only one term in the derivative, and rest of the derivatives will go to zero, because we are taking derivative wrt one variable, and others are constant
- its more like an if else condition, 
- how do we write in math, its called indicator variable, 
- ![](2023-10-09-19-21-54.png)
- 1 here means the indicator variable
- ![](2023-10-09-19-22-36.png)
- it just encodes if else condition
- so we can agree that the above two are same
- ![](2023-10-09-19-24-52.png)
- the above vector will have 1 only in one position and 0 in the remaining positions
- these kind of vectors are called one hot vector, represented as `el`, just a more compact way of writing the vector
- note h1,h2,h3 are 
- ![](2023-10-09-19-56-04.png)
- https://youtu.be/T6kfyQ3_JQ8?t=615
- first lets try to find L(theta)aLi
- what is loss function here?
    - -log(yhat l)
- ![](2023-10-09-20-01-06.png)
- what is yhatl?
    - it is the output of the softmax function
    - ![](2023-10-09-20-01-39.png)
- ![](2023-10-09-20-03-43.png)
- we are trying to compute the derivative of loss function with respect to one of element of L vector
- ![](2023-10-09-20-08-08.png)
- y hat is a vector
- al is a vector 
- softmax is a vector
- ![](2023-10-09-20-11-07.png)
- ![](2023-10-09-20-12-35.png)
- the derivative of `e**x is e**x`
- ![](2023-10-09-20-22-59.png)
- ![](2023-10-09-20-26-13.png)
- ![](2023-10-09-20-26-49.png)
- ![](2023-10-09-20-28-22.png)
- ![](2023-10-09-20-29-28.png)
- now we know that  , the gradient of the output layer, is the difference between the output of the softmax function, and the one hot vector
- talk to output layer is over
