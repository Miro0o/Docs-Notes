# Link-State (LS) Routing Algorithms

[TOC]



## Res


## Intro



## Dijkstra, Single-node Shortest Path
### Computational Complexity
What is the computational complexity of this algorithm? That is, given n nodes (not counting the source), how much computation must be done in the worst case to find the least-cost paths from the source to all destinations? In the first iteration, we need to search through all n nodes to determine the node, w, not in N" that has the minimum cost. In the second iteration, we need to check n - 1 nodes to determine the minimum cost; in the third iteration n - 2 nodes, and so on. Overall, the total number of nodes we need to search through over all the iterations is n(n + 1)/2, and thus we say that the preceding implementation of the LS algorithm has worst-case complexity of order n squared: O(n2). (A more sophisticated implementation of this algorithm, using a data structure known as a heap, can find the minimum in line 9 in logarithmic rather than linear time, thus reducing the complexity.)


### Oscillations

![](../../../../../../../Assets/Pics/Screenshot%202023-05-20%20at%201.47.53%20PM.png)


What can be done to prevent such oscillations (which can occur in any algo- rithm, not just an LS algorithm, that uses a congestion or delay-based link metric)? One solution would be to mandate that link costs not depend on the amount of traffic carried—an unacceptable solution since one goal of routing is to avoid highly con- gested (for example, high-delay) links. Another solution is to ensure that not all rout- ers run the LS algorithm at the same time. This seems a more reasonable solution, since we would hope that even if routers ran the LS algorithm with the same perio- dicity, the execution instance of the algorithm would not be the same at each node. Interestingly, researchers have found that routers in the Internet can self-synchronize among themselves [Floyd Synchronization 1994]. That is, even though they initially execute the algorithm with the same period but at different instants of time, the algo- rithm execution instance can eventually become, and remain, synchronized at the routers. One way to avoid such self-synchronization is for each router to randomize the time it sends out a link advertisement.




## Ref

