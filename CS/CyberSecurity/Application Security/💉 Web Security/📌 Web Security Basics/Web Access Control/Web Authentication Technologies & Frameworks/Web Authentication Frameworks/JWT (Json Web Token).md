# JWT (Json Web Token)

[TOC]



## Res
🏠 https://jwt.io

↗ [OKTA](../../../../../../../System%20Architecture%20Design/☁️%20Cloud%20Native/🌵%20Cloud%20Native%20Overview/🗿%20Cloud%20Models/Cloud%20Service%20(Delivery)%20Models/SaaS/Identity%20Cloud/OKTA/OKTA.md)
↗ [Auth0](../../../../../../../System%20Architecture%20Design/☁️%20Cloud%20Native/🌵%20Cloud%20Native%20Overview/🗿%20Cloud%20Models/Cloud%20Service%20(Delivery)%20Models/SaaS/Identity%20Cloud/OKTA/Auth0.md)



## Intro
> 🔗 https://jwt.io/introduction

JSON Web Token (JWT) is an open standard ([RFC 7519](https://tools.ietf.org/html/rfc7519)) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the **HMAC** algorithm) or a public/private key pair using **RSA** or **ECDSA**.

Although JWTs can be encrypted to also provide secrecy between parties, we will focus on _signed_ tokens. Signed tokens can verify the _integrity_ of the claims contained within it, while encrypted tokens _hide_ those claims from other parties. When tokens are signed using public/private key pairs, the signature also certifies that only the party holding the private key is the one that signed it.



## Ref
[So what the heck is JWT or JSON Web Token? | Medium]: https://medium.com/jspoint/so-what-the-heck-is-jwt-or-json-web-token-dca8bcb719a6

[不要用JWT替代session管理（上）：全面了解Token,JWT,OAuth,SAML,SSO - 李熠的文章 - 知乎]: https://zhuanlan.zhihu.com/p/38942172

[👍 一文搞懂Session和JWT登录认证 | Segmentfault]: https://segmentfault.com/a/1190000043668512

[JSON Web Tocken | Wikipedia]: https://en.wikipedia.org/wiki/JSON_Web_Token
