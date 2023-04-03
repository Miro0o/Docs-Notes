# JavaScript

[TOC]



## Res
### Opensource 
[You Dont Know JS](https://github.com/getify/You-Dont-Know-JS)

> This is a series of books diving deep into the core mechanisms of the JavaScript language. This is the **second edition** of the book series.
> 
> I recommend reading the **second edition** books in this order:
> - [Get Started](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/get-started/README.md) | [Buy on Leanpub](https://leanpub.com/ydkjsy-get-started) | [Buy on Amazon](https://www.amazon.com/dp/B084BNMN7T)
> - [Scope & Closures](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/README.md) | [Buy on Leanpub](https://leanpub.com/ydkjsy-scope-closures) | [Buy on Amazon](https://www.amazon.com/dp/B08634PZ3N)
> - [Objects & Classes](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/objects-classes/README.md) (draft stable)
> - [Types & Grammar](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/types-grammar/README.md) (draft in progress)
> - Sync & Async (not yet started)
> - ES.Next & Beyond (not yet started)
>
> If you're looking for the previous **first edition** books, [they can be found here](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/README.md).


### 🎥 Video:
- [翁恺老师讲JS](https://www.bilibili.com/video/BV1nJ41127Dc?p=2&share_source=copy_web)
  - HTML
     - CSS


### ☕️ Official:
- [JS](https://www.javascript.com) 
  - [Io.js](https://blog.risingstack.com/iojs-overview/) (now merged with JS. )
  
- [ECMA](https://tc39.es/ecma262/#sec-intro) 
- Node.js
  - [CN](https://www.w3schools.com/js/default.asp)
  - [EN](https://nodejs.org/en/docs/guides/)
- [npm](https://www.npmjs.com)
- [Vue](https://vuejs.org) 
- [Require.JS](https://requirejs.org/docs/commonjs.html) (a JS module loader)
  
  - AMD, CommonJS
  

###  🖥 Blogs:
- [廖雪峰](https://www.liaoxuefeng.com/wiki/1022910821149312)
- [菜鸟](https://www.runoob.com/nodejs/nodejs-tutorial.html)
- [W3C](https://www.w3schools.com/js/default.asp)
- [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)




## Overview
JavaScript （literally has nothing to do with  [Java](../../../../../🔑 CS_Core/Programming Lang/Compile/Java/Intro.md)） is initially a **script language** running on __browser side__, implementing simple interactive motions to the web page. However, as [node.js](https://nodejs.org/en/) ==(a js runtime env, allowing JS implemented on server host)== and other likes have gained popularity, JS was introduced to the beckend and start have a growing significant bearing in web dev. 

To support JavaScript running on any host, [Node.js](https://nodejs.org/en/) is a very popular runtime environment ([IO.js](https://blog.risingstack.com/iojs-overview/) is a fork from Node.js. move to this post [What is the difference between node.js and io.js?](https://stackoverflow.com/questions/27309412/what-is-the-difference-between-node-js-and-io-js) on StackOverflow to see more between Node.js&IO.js).

`npm` is a package maneger on Node.JS. parallel it as py on Python. 

[ECMA](https://tc39.es/ecma262/#sec-intro) ( European Computer Manufacturers Association) is the organization who set standards for JavaScript. 

Enjoy!


### History
Netscope -> Navigator -> JavaScript

The set of standard is referred as ECMAScript. 

> The JavaScript naming convention started with ES1, ES2, ES3, ES5 and ES6.
> But, ECMAScript 2016 and 2017 was not called ES7 and ES8.
> Since 2016 new versions are named by year (ECMAScript 2016 / 2017 / 2018).
> ref: https://www.w3schools.com/js/js_2018.asp

There were alos other Script language running on web side aside JavaScript from Netscope, like JScript from MicroSoft.   



## Refs

![The most satisfactory front-end frameworks](https://www.codica.com/static/8040ddc71ecb05b420068525e826fb6a/8cbf7/Satisfaction_ratio_rankings_of_front_end_frameworks_9a7de8798b.jpg "Satisfaction ratio rankings of front-end frameworks")
- [Vue.js vs React](https://www.codica.com/blog/react-vs-vue/)

![Top web frameworks the most used by professional developers](https://www.codica.com/static/414da4ed44f3b0f0ea51f9411e526aab/97b8c/The_most_commonly_used_web_frameworks_6d817565c4.jpg "The most commonly used web frameworks")

- [uni-app,Taro,react native和flutter的区别](https://blog.csdn.net/u011590754/article/details/115453390)
- [Relation between CommonJS, AMD and RequireJS?](https://stackoverflow.com/questions/16521471/relation-between-commonjs-amd-and-requirejs)
- [XHR (XMLHttpRequest)](https://developer.mozilla.org/en-US/docs/Glossary/XHR_(XMLHttpRequest))