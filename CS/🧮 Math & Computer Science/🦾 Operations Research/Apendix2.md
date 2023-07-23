作者：王源
链接：https://www.zhihu.com/question/22686770/answer/618437135
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



学习一门课程首先要了解学习的目的和意义。我们这里暂且不谈学好了运筹学能够走上人生巅峰，迎娶白富美的事情。这里只谈一小点学了运筹学的人和没有学运筹学的人的细微差别。我认为运筹学影响了我做事的方式。运筹学的基本套路是把实际问题建立模型，然后确定决策变量，其次确定优化目标和约束条件。其实在我们工作中和生活中去处理每一件事情的时候，都是可以通过这种方法来迅速抓住事物的本质，达到很高的做事效率的。而没有学过[运筹优化](https://www.zhihu.com/search?q=运筹优化&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})的人，则不会有这样的思维，以至于他们在做事情的时候并往往是不能有一套高效的运行机制。我想这个是学习运筹学给我带来的最大的一个启示。

## **1，基础课程**

老生常谈了，要入门运筹学最起码要有基本的数学知识。基本的要求也不高，微积分，[线性代数](https://www.zhihu.com/search?q=线性代数&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})，外加一门编程语言即可。

微积分和线性代数是所有理工科本科生的基础课程，所以这里也就不再赘述了。至于编程语言掌握一门主流编程语言即可，例如C,C++,Python,Java,Julia，因为最终优化问题的求解都要利用一些[solver](https://www.zhihu.com/search?q=solver&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})，都需要一门基础的编程语言做支撑。

如果上面所提的几个数学内容不是很自信的同学可以参考如下的视频课程，

[Essence of calculus](https://link.zhihu.com/?target=https%3A//www.youtube.com/playlist%3Flist%3DPLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)，作者以拉风的动画，深入的理解带你回顾一下微积分的关键概念。该课程的好处是直观清晰，都是短视频，适合曾经学过微积分但是又比较模糊的同学。

线性代数也是一样的 [Essence of linear algebra](https://link.zhihu.com/?target=https%3A//www.youtube.com/playlist%3Flist%3DPLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) 以非常直观的角度审视了线性代数的重要概念，直观但不失深刻，配合上高大上的动画效果，让人体会到了大道至简的感觉。一共15个视频，每段视频大约十分钟左右，花费不了多少时间就能看完。



## **2，中级课程**

线性规划(Linear Programming)+凸优化(Convex Optimization)+数值优化（Numerical Optimization)

1 线性规划就是目标和约束条件都是线性的了，其问题形式非常的简单，所以说线性规划是最基本的内容。线性规划肯定也是凸优化的一种，但是线性规划有着一些非常特殊的性质。个人感觉线性规划是基础的基础，往后边整数规划，[鲁棒优化](https://www.zhihu.com/search?q=鲁棒优化&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})，半定规划，锥优化等都离不开线性规划这个基础。学习线性规划需要 几何的直观感受+代数的精确描述+一些计算机的编程实际 三个维度。几何的直观感受可以给我们提供非常好的理解线性规划理论的途径，所以千万不要一上来就一顿代数计算，什么单纯型表进基出基一顿折腾，表上作业法搞得热火朝天的。一定一定要先理解几何的直观意义是什么，然后再用代数把直观感受严密表述出来，这时候一堆枯燥的代数公式就非常好理解了。最后当然需要一点计算机的实践，用solver求解一些问题获得一些应用的感受。

线性规划首推 [Dimitris Bertsimas](https://link.zhihu.com/?target=https%3A//book.douban.com/search/Dimitris%20Bertsimas) / [John N. Tsitsiklis](https://link.zhihu.com/?target=https%3A//book.douban.com/search/John%20N.%20Tsitsiklis) 的 [Introduction to Linear Optimization.pdf](https://link.zhihu.com/?target=https%3A//b-ok.org/book/1263070/ad9008)，这本书是一个比较现代的观念看线性规划了，包括了椭球法，单纯形法，[内点法](https://www.zhihu.com/search?q=内点法&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})，以前一些拓展内容和future work的方向。当然这本书只有前半段是线性规划内容，所以如果只想学线性规划的话 看完前半段即可，虽然他的后半段也极其精彩。

线性规划的视频课程我推荐 台湾交通大学的公开课，方述诚老师讲的线性规划（很不幸发现这个课程下架了 这里无法给出链接，有需要的后期我可以放网盘链接。方老师每次都从几何的直观出发，然后用代数去严密化直观的东西，具备一定的线性代数知识完全就能理解。



2 世界不总是线性的，优化问题向前一步就是凸优化了，相对[非凸优化](https://www.zhihu.com/search?q=非凸优化&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})，凸优化要相对容易一点。这里就绕不开 Stephen Boyd 的 convex optimization 那本书了。这本书是主要分为理论、应用和算法三个层面。其实初学者的困惑有几个，1是书中会用到一些矩阵变换或者不等式放缩的东西。这说明你的数学基础有待提高，2很多同学即使能看懂推导过程也不明白为何要有这些一大堆的理论。这个问题就比较困难一点说明你在优化领域涉及不深，同时对实际应用问题感悟也很少。

其实对于凸优化而言真正的难点是在实际的科研和工程问题中，怎么把你的模型建立成凸优化问题，或者怎么样变换成凸优化问题。这个技巧往往是一门艺术了，没有很一般的方法，具体问题具体看待，好在Stephen Boyd的convex optimization这本书在应用这部分给我们举了很多例子，初学者还一下子get不到这里边的妙处，只有真正做过应用问题的回来再看就很有感受。

Stephen Boyd 的 Convex optimization，与之配套的视频课程也有[Convex optimization](https://link.zhihu.com/?target=https%3A//freevideolectures.com/course/2288/convex-optimization-i)

如果想深入一点可以看 [Introductory Lectures on Convex Programming.pdf](https://link.zhihu.com/?target=http%3A//citeseerx.ist.psu.edu/viewdoc/download%3Fdoi%3D10.1.1.693.855%26rep%3Drep1%26type%3Dpdf)



3 数值优化是我个人比较推荐的一个课程，其实数值优化侧重算法一点，而不像前面的线性规划和凸优化需要一大堆的理论框架（虽然这些理论都很美）。数值优化很大一部分就是基于导数的优化方法，这类方法在机器学习里边是最常见应用最广泛的。数值优化的理论分析一般侧重于收敛性和[收敛速率](https://www.zhihu.com/search?q=收敛速率&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})，所以它的理论是比较单纯一些的。

数值优化推荐的书自然是 [Numerical Optimization.pdf](https://link.zhihu.com/?target=http%3A//www.bioinfo.org.cn/~wangchao/maa/Numerical_Optimization.pdf)

国内有一个相关的视频课程讲得也不错可供参考：[数值优化-复旦大学吴立德](https://link.zhihu.com/?target=https%3A//www.bilibili.com/video/av10289610/)

上述三门课程的教材和视频课程资源已经被整理到如下链接中可以获取：



## **3 高级课程**

多目标优化、[随机优化](https://www.zhihu.com/search?q=随机优化&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})、鲁棒优化、整数规划，混合整数规划，动态规划，[元启发式算法](https://www.zhihu.com/search?q=元启发式算法&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A618437135})、半正定规划等等高级课程这里就无法一一去点评了，如果具备了之前的基础相信去学这些高级课程会轻松一些。