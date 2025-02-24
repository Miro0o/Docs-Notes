# Optimizing 
###  0. [gradient & SGD](https://www.zhihu.com/question/29151564)
[SGD](https://www.zhihu.com/question/264189719)
[scikit-learn : SGD](https://scikit-learn.org/stable/modules/sgd.html)


### 1. genetic algorithm
##### steps:
1. set population scale (data scale)
2. emulate evolution (set objective solution )
	1. genetic recombination 
	2. genetic mutation (set mutate scope)
3. natural selection (sort & select the top instances to form the new generation )
4. another new round of evolve. 

##### comments:
seems like a randomized brute-force exhaustive search algorithm with some prune?? in this case, by step 3 'natural selection', the algorithm cuts off the redundant possibilities at some scale, thus cuts off some scope needed for brute-force exhaustive search algorithm. the correctness of this algorithm lies in the step 2 'emulate evolution'. By introducing data recombination and random data within the possible solution scope, it makes sure every possible solution is under cover. 

#### 遗传算法：
##### 算法步骤：
1. 确立种群规模 （目标数据集）
2. 模拟进化
	1. 基因重组 （在现有数据集范围内，搜索可能的状态）
	2. 基因突变 （加入新的数据集，新的数据集不属于当前数据集，但是属于所有可能解构成的数据集，这样构成一个新的范围，在这个范围内搜索可能的状态）
3. 自然选择 （模拟进化步骤后，当前数据集是目标数据集的2倍，所以要在这个新的2倍的数据集里按目标数据集的标准（即进化方向）减去一半）
4. 重复，直至达到目标种群（得到目标解）或重复次数达到约定次数

##### 个人理解：
遗传算法本质是一个带有剪枝的搜索。基因重组和基因突变保证了所有可能解都会被搜索到，而自然选择则保证了每一次搜索结果和目标结果的吻合度不低于上一次搜索结果。所以理论上只要搜索次数够大，就一定能最后逼近目标结果。一些效率问题在于，1.模拟进化的步骤需要同时处理很多数据集，这些数据集很多是冗余的2.模拟进化的时候，基因重组和突变带来的变化是随机的，这有可能导致不必要的搜素。

### 2. [Simulating Anealling ](https://towardsdatascience.com/optimization-techniques-simulated-annealing-d6a4785a1de7)


#### [退火算法](https://zhuanlan.zhihu.com/p/266874840)