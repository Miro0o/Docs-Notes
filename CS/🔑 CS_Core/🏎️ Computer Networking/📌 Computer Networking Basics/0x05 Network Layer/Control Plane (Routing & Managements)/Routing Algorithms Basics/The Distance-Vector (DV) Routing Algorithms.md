# The Distance-Vector (DV) Routing Algorithm

[TOC]



## Res


## Intro

> DV-like algorithms are used in many routing protocols in practice, including the Internet’s RIP and BGP, ISO IDRP, Novell IPX, and the original ARPAnet.


Whereas the LS algorithm is an algorithm using global information, the **distance-vector (DV) algorithm** is **iterative**, **asynchronous**, and **distributed**. 
- It is **distributed** in that each node receives some information from one or more of its directly attached neighbors, performs a calculation, and then distributes the results of its calculation back to its neighbors. 
- It is **iterative** in that this process continues on until no more information is exchanged between neighbors. (Interestingly, the algorithm is also **self-terminating** -- there is no signal that the computation should stop; it just stops.) 
- The algorithm is **asynchronous** in that it does not require all of the nodes to operate in lockstep with each other.

We’ll see that an asynchronous, iterative, self-terminating, distributed algorithm is much more interesting and fun than a centralized algorithm!


### Bellman-Ford Equation
$$d_x(y) = min_v\{c(x, v) + d_v(y)\}$$

where the $min_v$ in the equation is taken over all of x’s neighbors. The Bellman-Ford equation is rather intuitive. Indeed, after traveling from x to v, if we then take the least-cost path from v to y, the path cost will be $c(x, v) + d_v(y)$. Since we must begin by traveling to some neighbor v, the least cost from x to y is the minimum of $c(x, v) + d_v(y)$ taken over all neighbors v.

The Bellman-Ford equation is not just an intellectual curiosity. It actually has significant practical importance: 

- the solution to the Bellman-Ford equation provides the entries in node x’s forwarding table. 

> To see this, let v* be any neighboring node that achieves the minimum in equation above. Then, if node x wants to send a packet to node y along a least-cost path, it should first forward the packet to node v*. Thus, node x’s forwarding table would specify node v* as the next-hop router for the ultimate destination y. 

- Another important practical contribution of the Bellman-Ford equation is that it suggests the form of the neighbor-to-neighbor communication that will take place in the DV algorithm.




## BF Algorithm




## Ref

