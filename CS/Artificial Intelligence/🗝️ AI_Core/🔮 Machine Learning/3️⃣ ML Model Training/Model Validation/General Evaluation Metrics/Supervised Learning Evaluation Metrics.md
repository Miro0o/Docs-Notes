# Supervised Learning Evaluation Metrics

[TOC]



## Res


## Intro


## Accuracy & Loss


## Confusion Matrix



## Ref
[🤔 What is the relationship between the accuracy and the loss in deep learning? | Stack exchange ]: https://datascience.stackexchange.com/questions/42599/what-is-the-relationship-between-the-accuracy-and-the-loss-in-deep-learning

There is no relationship between these two metrics.   
Loss can be seen as a **distance** between the true values of the problem and the values predicted by the model. Greater the loss is, more huge is the errors you made on the data.

Accuracy can be seen as the **number** of error you made on the data.

That means:  
- a low accuracy and huge loss means you made huge errors on a lot of data  
- a low accuracy but low loss means you made little errors on a lot of data  
- a great accuracy with low loss means you made low errors on a few data (best case)  
- your situation: a great accuracy but a huge loss, means you made huge errors on a few data.

For you case, the third model can correctly predict more examples, but on those where it was wrong, it made more errors (the distance between true value and predicted values is more huge).

**NOTE:**
Don't forget that low or huge loss is a subjective metric, which **depends** on the problem and the data. It's a distance between the true value of the prediction, and the prediction made by the model. It depends also on the loss you use.  

Think:  
- If your data are between 0 and 1, a loss of 0.5 is huge, but if your data are between 0 and 255, an error of 0.5 is low.  
- Maybe think of cancer detection, and probability of detecting a cancer. Maybe an error of 0.1 is huge for this problem, whereas an error f 0.1 for image classification is fine.


[👍 Train Accuracy vs Test Accuracy vs Confusion matrix]: https://datascience.stackexchange.com/questions/28426/train-accuracy-vs-test-accuracy-vs-confusion-matrix

[What is the difference between the terms accuracy and validation accuracy? | Stackoverflow]: https://stackoverflow.com/a/51345413/16542494
