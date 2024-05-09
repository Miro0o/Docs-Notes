# Helm

[TOC]



## Res
🏠 https://helm.sh
🚧 https://github.com/helm/helm


### Related Topics
↗ [K8s](../../../../Cloud%20Operating%20System%20&%20Platform%20(System%20Level%20Engineering)/🥋%20Orchestration%20&%20Management/Cluster%20Scheduling%20&%20Orchestration/🏗️%20K8s/K8s.md)



## Intro
Helm is a tool for managing Charts. Charts are packages of pre-configured Kubernetes resources.

Helm is a tool that streamlines installing and managing Kubernetes applications. Think of it like apt/yum/homebrew for Kubernetes.

What Helm do:
- Helm renders your templates and communicates with the Kubernetes API
- Helm runs on your laptop, CI/CD, or wherever you want it to run.
- Charts are Helm packages that contain at least two things:
    - A description of the package (`Chart.yaml`)
    - One or more templates, which contain Kubernetes manifest files
- Charts can be stored on disk, or fetched from remote chart repositories (like Debian or RedHat packages)

Use Helm to:
- Find and use [popular software packaged as Helm Charts](https://artifacthub.io/packages/search?kind=0) to run in Kubernetes
- Share your own applications as Helm Charts
- Create reproducible builds of your Kubernetes applications
- Intelligently manage your Kubernetes manifest files
- Manage releases of Helm packages



## Ref

