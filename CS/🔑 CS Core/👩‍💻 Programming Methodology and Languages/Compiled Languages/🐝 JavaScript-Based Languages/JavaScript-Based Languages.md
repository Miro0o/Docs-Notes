# JavaScript-Based Languages

[TOC]



## Res
📂 https://tc39.es/ecma262/#sec-intro 
ECMA

📂 🇨🇳 https://www.w3schools.com/js/default.asp
📂 🇺‍🇸 https://nodejs.org/en/docs/guides/

📂 https://developer.mozilla.org/en-US/docs/Web/JavaScript/
MDN Web Docs


### Related Topics
↗ [JavaScript Runtime Environments](../../🛠️%20Programming%20Tools%20Chain/🚠%20Application%20Runtimes%20&%20SDKs/JavaScript%20Runtime%20Environments/JavaScript%20Runtime%20Environments.md)
↗ [Microsoft](../../../Electronics%20&%20Information%20Technologies%20Business%20Fields%20Research/📌%20Comprehensive%20Electronics%20&%20Information%20Technology%20Services/Microsoft.md)

↗ [JavaScript (Browser End)](../../../../Software%20Engineering/Web%20Development/🖥️%20Web%20FrontEnd%20Dev/📌%20Web%20Frontend%20Basics/JavaScript%20(Browser%20End)/JavaScript%20(Browser%20End).md)
↗ [JS Frameworks for FrontEnd](../../../../Software%20Engineering/Web%20Development/🖥️%20Web%20FrontEnd%20Dev/📌%20Web%20Frontend%20Basics/🎃%20JS%20Frameworks%20for%20FrontEnd/JS%20Frameworks%20for%20FrontEnd.md)


### JS Standards


### Learning Resources
[廖雪峰](https://www.liaoxuefeng.com/wiki/1022910821149312)
[菜鸟](https://www.runoob.com/nodejs/nodejs-tutorial.html)

🎬 [翁恺老师讲JS](https://www.bilibili.com/video/BV1nJ41127Dc?p=2&share_source=copy_web)

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

[JS](https://www.javascript.com) 
- [Io.js](https://blog.risingstack.com/iojs-overview/) (now merged with JS. )

[Require.JS](https://requirejs.org/docs/commonjs.html) (a JS module loader)
- AMD, CommonJS



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



## JavaScript Implementations
> ↗ [JavaScript Runtime Environments](../../🛠️%20Programming%20Tools%20Chain/🚠%20Application%20Runtimes%20&%20SDKs/JavaScript%20Runtime%20Environments/JavaScript%20Runtime%20Environments.md)


### JS engines for Browser/Server 
- Mozilla's [SpiderMonkey](https://spidermonkey.dev/), used in Firefox. This was the first _ever_ JavaScript engine, created by Brendan Eich at Netscape.
- Google's [V8](https://v8.dev/), used in Google Chrome, Opera, Edge, [Node.js](https://nodejs.org/), [Deno](https://deno.land/), [Electron](https://www.electronjs.org/), and more.
- Apple's [JavaScriptCore](https://trac.webkit.org/wiki/JavaScriptCore) (also known as SquirrelFish/Nitro), used in WebKit browsers such as Apple Safari, and [Bun](https://bun.sh/).


### JS engines specifically for non-browser purpose
- [Engine262](https://engine262.js.org/), a JavaScript engine written in JavaScript. It is created for JavaScript developers to explore new language features and find bugs in the specification.
- [Moddable XS](https://www.moddable.com/), used in embedded systems such as IoT.
- [QuickJS](https://bellard.org/quickjs/), a small and embeddable JavaScript engine.
- Meta's [Hermes](https://hermesengine.dev/) engine, an engine optimized for [React Native](https://reactnative.dev/docs/hermes).
- Oracle's [GraalJS](https://www.graalvm.org/), a high performance implementation built on the GraalVM by Oracle Labs.


### Legacy JS Implementations
- [Carakan](https://dev.opera.com/blog/carakan-faq/), used in earlier versions of Opera.
- Microsoft's [Chakra](https://en.wikipedia.org/wiki/Chakra_(JScript_engine)) engine, used in Internet Explorer (although the language it implements is formally called "JScript" to avoid trademark issues). Earlier versions of Edge used a new JavaScript engine, confusingly also called [Chakra](https://en.wikipedia.org/wiki/Chakra_(JavaScript_engine)).
- [LibJS](https://libjs.dev/), used in the browser implementation of [SerenityOS](https://serenityos.org/).
- Mozilla's [Rhino](https://en.wikipedia.org/wiki/Rhino_(JavaScript_engine)) engine, a JavaScript implementation written in Java, created primarily by Norris Boyd (also at Netscape).

JavaScript

ActionScript



## JS Shell
A JavaScript shell allows you to quickly test snippets of JavaScript code without having to reload a web page. They are extremely useful for developing and debugging code.


### Standalone JavaScript shells
The following JavaScript shells are stand-alone environments, like Perl or Python.
- [Node.js](https://nodejs.org/) - Node.js is a platform for easily building fast, scalable network applications.
- [ShellJS](https://github.com/shelljs/shelljs) - Portable Unix shell commands for Node.js.


### Browser-based JavaScript shells
The following JavaScript shells run code through the browser's JavaScript engine.

- Firefox has a [built-in JavaScript console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html), which support multi-line editing.
- [Babel REPL](https://babeljs.io/repl) - A browser-based [REPL](https://en.wikipedia.org/wiki/REPL) for experimenting with future JavaScript.
- [TypeScript playground](https://www.typescriptlang.org/play) — A browser-based playground for experimenting both new JavaScript features (via the tsc compiler) and TypeScript syntax.



## Refs
![The most satisfactory front-end frameworks](https://www.codica.com/static/8040ddc71ecb05b420068525e826fb6a/8cbf7/Satisfaction_ratio_rankings_of_front_end_frameworks_9a7de8798b.jpg "Satisfaction ratio rankings of front-end frameworks")
- [Vue.js vs React](https://www.codica.com/blog/react-vs-vue/)

![Top web frameworks the most used by professional developers](https://www.codica.com/static/414da4ed44f3b0f0ea51f9411e526aab/97b8c/The_most_commonly_used_web_frameworks_6d817565c4.jpg "The most commonly used web frameworks")
- [uni-app,Taro,react native和flutter的区别](https://blog.csdn.net/u011590754/article/details/115453390)
- [Relation between CommonJS, AMD and RequireJS?](https://stackoverflow.com/questions/16521471/relation-between-commonjs-amd-and-requirejs)
- [XHR (XMLHttpRequest)](https://developer.mozilla.org/en-US/docs/Glossary/XHR_(XMLHttpRequest))

[TypeScript的4种编译方式 | cnblog]: https://www.cnblogs.com/malcolmfeng/p/9375963.html

JavaScript 是于1996年被开发出来的，然后在1997年被提交给 ECMA 国际用于标准化工作，这导致了 ECMAScript 的诞生。同时，由于 JavaScript 与 ECMAScript 规范保持一致，所以可以说 JavaScript 是根据 ECMAScript 所实现的一个例子。因此令我们感到有趣的是：ECMAScript 是基于 JavaScript 的，而同时 JavaScript 又是基于 ECMAScript 的。

TypeScript是微软开发的一门脚本语言，它是JavaScript的超集，它遵循ES6语言规范。ES5，ES6都是脚本语言的规范，JavaScript和TypeScript是两种脚本语言。JavaScript实现了ES5，TypeScript实现了ES6

