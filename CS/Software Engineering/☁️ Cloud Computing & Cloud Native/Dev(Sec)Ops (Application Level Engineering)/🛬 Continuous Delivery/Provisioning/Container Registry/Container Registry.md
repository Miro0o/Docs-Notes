# Container Registry

[TOC]



## Res
📂 https://landscape.cncf.io/guide#provisioning--container-registry



## Intro
Before diving into container registries, we need to define three tightly related concepts:

- **Container** is "a running process with resource and capability constraints managed by a computer’s operating system" ([Cloud Native Glossary](https://github.com/cncf/glossary/blob/main/content/en/container.md)).
- **Image** is a set of archive files needed to run containers and its process. You could see it as a form of template on which you can create an unlimited number of containers.
- **Repository**, or just repo, is a space to store images.

And **container registries** are specialized web applications that categorize and store repositories.

Let's recap real quick: images contain the information needed to execute a program (within a container) and are stored in repositories which in turn are categorized and grouped in registries. Tools that build, run, and manage containers need access to those images. Access is provided by referencing the registry (the path to access the image).



## Ref

