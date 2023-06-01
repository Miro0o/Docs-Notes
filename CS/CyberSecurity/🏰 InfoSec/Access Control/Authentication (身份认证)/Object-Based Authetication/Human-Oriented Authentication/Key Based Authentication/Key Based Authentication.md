# Key Based Authentication

[TOC]



## Res


## Intro


## Certification Based (基于证书) (Asymmetric Key Based)
Generally, for certificate-based authentication, the system will generate a digital certificate to validate the user. It can be generated from the user’s unique Id like voter ID, passport, or other. It contains the user’s public key and digital signature, with this system will identify the right user, A system takes a digital sign from a user and uses cryptography to make sure it’s a valid user. 



## Token Based (基于令牌) (Symmetric Key Based)
Token-based authentication is a process in which users identify with unique tokens after the user provides credentials to the system. A token is valid only for a designated time period, after that user needs to re-generate it to use again. 

> ⚠ **Diff between certification & token**
>
> Tokens are essentially symmetric keys. That means that the same key has to be both on the client and the server to be able to authenticate users.
>
> Certificates use an asymmetric set of keys. Certificates are based on public-key cryptography. The client keeps possession of the private, which is never shared by anyone else.
>
> In Web Security, instead of just signing a ‘challenge’, the client signs the entirety of the message that’s sent by the server.



## Ref

