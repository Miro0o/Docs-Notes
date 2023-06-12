# Bellman-Ford Algorithm

[TOC]



## Res


## Intro
### Bellman-Ford Equation
$$d_x(y) = min_v\{c(x, v) + d_v(y)\}$$

where the $min_v$ in the equation is taken over all of x’s neighbors. The Bellman-Ford equation is rather intuitive. Indeed, after traveling from x to v, if we then take the least-cost path from v to y, the path cost will be $c(x, v) + d_v(y)$. Since we must begin by traveling to some neighbor v, the least cost from x to y is the minimum of $c(x, v) + d_v(y)$ taken over all neighbors v.

The Bellman-Ford equation is not just an intellectual curiosity. It actually has significant practical importance: 

- the solution to the Bellman-Ford equation provides the entries in node x’s forwarding table. 

> To see this, let v* be any neighboring node that achieves the minimum in equation above. Then, if node x wants to send a packet to node y along a least-cost path, it should first forward the packet to node v*. Thus, node x’s forwarding table would specify node v* as the next-hop router for the ultimate destination y. 

- Another important practical contribution of the Bellman-Ford equation is that it suggests the form of the neighbor-to-neighbor communication that will take place in the DV algorithm.



## BF Algorithm



## Ref

