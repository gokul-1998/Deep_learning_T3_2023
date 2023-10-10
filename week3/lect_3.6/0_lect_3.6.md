## 3.6 Gradient w.r.t Hidden Units

- Backpropagation: Computing  Gradients wrt Hidden Units

- ![](2023-10-09-23-09-18.png)
- h2 is hidden layer
- ![](2023-10-09-23-19-00.png)
- ![](2023-10-09-23-20-24.png)
- ![](2023-10-09-23-22-50.png)
- hij -> i is the layer number, j is the unit number
- k is the no of paths from the unit j in layer i to the output layer
- m is the no of units in the output layer
- ![](2023-10-09-23-27-46.png)
- the first term is already computed, we just need to compute the second term   
- ![](2023-10-09-23-31-29.png)
- red guys is the entire h2 vector
- ![](2023-10-09-23-44-33.png)
- ![](2023-10-09-23-46-35.png)
- https://youtu.be/7g-THFmBpRA?t=906