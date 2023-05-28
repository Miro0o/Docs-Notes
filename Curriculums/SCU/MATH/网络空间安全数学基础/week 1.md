+ 毕达哥拉斯
	+ 完美数
	+  同余
+ 欧几里得
+ 费马
+ 欧拉
+ 高斯
+ 通讯保密
+ > *TeX [syntex](https://zinglix.xyz/2017/08/23/latex-maths-cheatsheet/) 

# 1. 数论

+ [Euclid除法](https://blog.csdn.net/weixin_43886797/article/details/85569998)
+ [扩展欧几里得算法](https://blog.csdn.net/u014634338/article/details/40210435)
+ [算数基本定理](https://www.cnblogs.com/JustinRochester/p/12340602.html) （质因数分解）
+ [有理数性质](https://www.zhihu.com/question/377650865)
+ [Dirichlet 定理](https://zhuanlan.zhihu.com/p/57379991)
	+ 形如 $qn+l$ 的等差数列中包含无数个素数，当 $(q,l)=1$
	+ 则 $4k +1$ 等素数有无限个 （作业）
	+ [特殊形式素数无穷性的证明](https://blog.csdn.net/Gosick_Geass_Gate/article/details/86484915?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-86484915-blog-88873278.pc_relevant_multi_platform_featuressortv2dupreplace&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-86484915-blog-88873278.pc_relevant_multi_platform_featuressortv2dupreplace&utm_relevant_index=7)
	+  [无穷多的质数](https://sqr5.wordpress.com/2022/04/01/%e6%97%a0%e7%a9%b7%e5%a4%9a%e7%9a%84%e8%b4%a8%e6%95%b0/) 
+ 非完全平方数开根号为**无理数**
+ 贝祖等式 
	+ $s*a+t*b=(a,b)$
	+ [Goldbach's conjecture]()
+ [梅森数](https://zhuanlan.zhihu.com/p/82356370)
+ [剩余系，剩余定理，同余定理，费马小定理的证明](https://blog.csdn.net/acm_1361677193/article/details/47377119)
+ [质数的判定与筛法](https://blog.csdn.net/weixin_43810158/article/details/88112736)
	+ 质数的判定定理
		+ 任一数最小因数（除了1）小于其本身开根
			+ 对任一数，若 2 ～ √n 内都无n因数，则n为质数
		+ ==任一数最大质因数小于 √n==
			 + ☝️ 埃氏筛和欧氏筛基本思想 
	+ 质数定理
		+  n充分大时，n以内的素数个数约等于n/logn个。（仅做了解，并不具体说明）。
	+  质数筛法
		+ [埃拉托斯特尼筛法](https://zhuanlan.zhihu.com/p/151432852)
		+ [欧拉筛法](https://www.cnblogs.com/A-S-KirigiriKyoko/articles/6034572.html)
```c++
// Euler  

#include <cstring>
using namespace std;
int prime[1100000],primesize,phi[11000000];
bool isprime[11000000];
void getlist(int listsize)
{
    memset(isprime,1,sizeof(isprime));
    isprime[1]=false;
    for(int i=2;i<=listsize;i++)
    {
        if(isprime[i])prime[++primesize]=i;
         for(int j=1;j<=primesize&&i*prime[j]<=listsize;j++)
         {
            isprime[i*prime[j]]=false;
            if(i%prime[j]==0)break;
        }
    }
}

//  phi 
void getlist(int listsize)
{
    memset(isprime,1,sizeof(isprime));
    isprime[1]=false;
    for(int i=2;i<=listsize;i++)
    {
        if(isprime[i])
        {
             prime[++primesize]=i;
             phi[i]=i-1;
         }
         for(int j=1;j<=primesize&&i*prime[j]<=listsize;j++)
         {
            isprime[i*prime[j]]=false;
            if(i%prime[j]==0)
             {
                phi[i*prime[j]]=phi[i]*prime[j];
                break;
            }
            phi[i*prime[j]]=phi[i]*(prime[j]-1);
        }
    }
}


/*埃拉托斯特尼筛法,原理一个合数一定有小于等于sqrt(n)的素因子，
把所有这些素因子的倍数全部划去，那么剩下的就全是素数了*/
#include<bits/stdc++.h>
using namespace std;
const int Maxn=1e7;
bool vis[Maxn];
int prime[1000005];
int main()
{
	int n;
	cin>>n;
	prime[0]=0;
	memset(vis,false,sizeof(vis));
	for(int i=2;i<=sqrt(n);i++)
	{
		if(!vis[i])
		{
			vis[i]=true;
			prime[++prime[0]]=i;
			for(int j=i*i;j<=n;j+=i){
			vis[j]=true;
		}
		}
		
	}
	for(int i=sqrt(n)+1;i<=n;i++)
	{
		if(!vis[i])
		{
			prime[++prime[0]]=i;
		}
	}
	for(int i=1;i<=prime[0];i++) cout<<prime[i]<<endl;
} 


```


## 同余
🤔🤔 没有想通为什么？？？
书上📖说只有数K和P互质时才可以有$A \equiv B \pmod P$  <==> $K\times A \equiv K\times B \pmod P$， 但是我没有理解为什么一定要互质？？

> 若今天是周四，那么 2^2003天后是周几?
	> $1\equiv 8 \equiv 2^3\pmod 7$
	> $1^n\equiv 8^n \equiv 2^{3n}\pmod 7$
	> $2^{2003}=N \times 2^{3n} \times 2^2$
	> $\Rightarrow2^{2003} \equiv 2^2 \times1 \pmod 7$
	> $\Rightarrow$ Tus

+ [弃九法](https://blog.csdn.net/y11201/article/details/8623455)
+ 费马小定理
	> 费马小定理是初等[数论](https://baike.baidu.com/item/%E6%95%B0%E8%AE%BA)四大定理（[威尔逊定理](https://baike.baidu.com/item/%E5%A8%81%E5%B0%94%E9%80%8A%E5%AE%9A%E7%90%86)，[欧拉定理](https://baike.baidu.com/item/%E6%AC%A7%E6%8B%89%E5%AE%9A%E7%90%86)（数论中的欧拉定理），中国剩余定理(又称[孙子定理](https://baike.baidu.com/item/%E5%AD%99%E5%AD%90%E5%AE%9A%E7%90%86)），费马小定理）之一，在[初等数论](https://baike.baidu.com/item/%E5%88%9D%E7%AD%89%E6%95%B0%E8%AE%BA)中有着非常广泛和重要的应用。实际上，它是欧拉定理的一个特殊情况（即![](https://bkimg.cdn.bcebos.com/formula/883b26489df019421e297d75c8d31d0a.svg)，见于词条“[欧拉函数](https://baike.baidu.com/item/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0)”。 ^3a359b

	+ $A^P \equiv A \pmod P$
	+   即，A 和 $A^P$ 同属于一个P 的剩余类。
	+   由此可得 $A^{P-1} \equiv 1 \pmod P$ , 即$A \times A^{P-2} \equiv 1 \pmod P$ ,可以用这种方法求A关于P的逆元。==注意条件P为素数==。
	> 书上说只有数K和P互质时才可以有$A \equiv B \pmod P$ 等价于 $K\times A \equiv K\times B \pmod P$， 但是我没有理解为什么一定要互质？？
	+ 关于逆元和其他求逆元的方法见[[../../../../CS/🔑 CS_Core/🦄 Algorithm & Data Structure/OI-ICPC/Math (Discrete Mathematics)/Math (Discrete Mathematics)#同余|同余]]。
+ 简化剩余系与欧拉定理

