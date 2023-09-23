### Faster Higher and Stronger

![](2023-09-23-07-33-17.png)
![](2023-09-23-07-34-24.png)
![](2023-09-23-07-36-00.png)
- optimization Algorithms
    - Adagrad - Adaptive Gradient Descent
        - it is a type of Gradient Descent, where the learning rate is adaptive - it is not fixed 
    - RMSProp - Root Mean Square Propagation 
        
    - Adam - Adam is a combination of Adagrad and RMSProp
        - it is a type of Gradient Descent, where the learning rate is adaptive - it is not fixed 
        - it is a combination of Adagrad and RMSProp
    - NAdam - NAdam is a combination of Adam and Nesterov Momentum
        - it is a type of Gradient Descent, where the learning rate is adaptive - it is not fixed 
        - it is a combination of Adam and Nesterov Momentum
    - AdamW - AdamW is a combination of Adam and Weight Decay
        - it is a type of Gradient Descent, where the learning rate is adaptive - it is not fixed 
        - it is a combination of Adam and Weight Decay
    - RAdam - Rectified Adam
        - it is a type of Gradient Descent, where the learning rate is adaptive - it is not fixed 
        - it is a combination of Adam and Weight Decay
    - AdaBound - Adaptive Bound
        - it is a type of Gradient Descent, where the learning rate is adaptive - it is not fixed 
        - it is a combination of Adam and Weight Decay

![](2023-09-23-07-39-38.png)
![](2023-09-23-07-40-39.png)

- The above are better optimization algorithms 
- Now we will see better activation functions
![](2023-09-23-07-41-33.png)
- They are
    - ReLU - Rectified Linear Unit
    - Logistic Sigmoid - Logistic Sigmoid
    - Tanh - Hyperbolic Tangent
    - Leaky ReLU - Leaky Rectified Linear Unit
    - ELU - Exponential Linear Unit
    - GELU - Gaussian Error Linear Unit
    - SELU - Scaled Exponential Linear Unit
    - Swish - Swish
    - PFReLU - Parametric Flexible Rectified Linear Unit

![](2023-09-23-07-43-06.png)

- Better Regularization was also developed
    - Dropout
    - Batch Normalization
    - Weight Decay
    - Early Stopping
    - Data Augmentation
    - Mixup
    - Cutout
    - CutMix
    - MixMatch
    - MixNet

### Chapter - 6 : The curious case of Sequences

- ![](2023-09-23-07-46-41.png)
![](2023-09-23-07-48-41.png)
![](2023-09-23-07-49-13.png)
- Jordan Network 
    - this is a type of Recurrent Neural Network (RNN)
    - it allowed the output of the previous time step to be fed as input to the current time step
![](2023-09-23-07-51-00.png)
- Drawbacks of RNN
    - ![](2023-09-23-07-51-40.png)
    - Exploding Gradient
        - the gradients become very large and the weights become very large
    - Vanishing Gradient
        - the gradients become very small and the weights become very small
![](2023-09-23-07-53-19.png)
![](2023-09-23-07-53-55.png)
![](2023-09-23-07-54-42.png)

### Chapter - 7 : Beating humans at their own game(literally)

RL - Reinforcement Learning
    - ![](2023-09-23-07-58-21.png)
    - Google DeepMind's Deep Q-learning playing Atari
    - https://www.youtube.com/watch?v=V1eYniJ0Rnk
    - PAcman and pingpong are also played by DeepMind's Deep Q-learning

![](2023-09-23-08-00-56.png)
- DNQs Alpha-Go 
![](2023-09-23-08-02-50.png)
![](2023-09-23-08-03-17.png)
![](2023-09-23-08-04-47.png)
![](2023-09-23-08-05-33.png)
![](2023-09-23-08-05-45.png)
![](2023-09-23-08-06-51.png)
- https://www.youtube.com/watch?v=kopoLzvh5jY&pp=ygUQaGlkZSBhbmQgc2VlayBhaQ%3D%3D

![](2023-09-23-08-08-59.png)
![](2023-09-23-08-10-03.png)