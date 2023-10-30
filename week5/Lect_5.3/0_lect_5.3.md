## 5.3 RMSProp

- Lets see if we can do something to avoid the accumulation of b
- We are allowing to grow un inhibitedly, because its just accumulating the squares, so now frequent parameters will start receiving small updates, can we avoid this and prevent the rapid  growth of the denominator, can we try to scale down the growth of the denominator, and we know how to do that 
- ![](2023-10-30-08-23-05.png)
- instead of the original equation which was allowing the gradients to get added ,we can take a fraction of the gradient 
- if typical value of Beta , say 0.9
- 1-Beta = (0.1 * the gradient) 
- history continuously gets multiplied by 0.9, so whatever was my accumulated history has become 0.9 times, and my current gradient , also we are not taking it fully , we are also taking fraction of it, so thats why we are not allowing the history to grow as rapidly, as it was growing in the case of adagrad
- This is the change we have made in RMS Prop
- the update rule remains the same, and everything else remains the same  
- the only thing that has change is the denominator vt , earlier it was growing rapidly, now it is growing slowly
- we have added a new hyper parameter Beta, which is typically 0.9, and hence Beta and 1-Beta,are both less than 1, so we are multiplying the history by a fraction, and we are also multiplying the gradient by a fraction, so we are not allowing the history to grow as rapidly as it was growing in the case of adagrad
- ![](2023-10-30-08-29-00.png)
- ![](2023-10-30-08-32-06.png)
- we can see that history is exponentially decaying, because  earlier we were taking the whole of b0**2, but now we are taking a small fraction of it
- so now we are controlling the rate at which v2 is growing , im not allowing it to shoot quixkly, im doing this exponentially decaying average
