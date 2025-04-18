# Cloud Custodian (c7n)

[TOC]



## Res
🚧 https://github.com/cloud-custodian/cloud-custodian



## Intro
> Rules engine for cloud security, cost optimization, and governance, DSL in yaml for policies to query, filter, and take actions on resources

Cloud Custodian, also known as c7n, is a rules engine for managing public cloud accounts and resources. It allows users to define policies to enable a well managed cloud infrastructure, that's both secure and cost optimized. It consolidates many of the adhoc scripts organizations have into a lightweight and flexible tool, with unified metrics and reporting.

Custodian can be used to manage AWS, Azure, and GCP environments by ensuring real time compliance to security policies (like encryption and access requirements), tag policies, and cost management via garbage collection of unused resources and off-hours resource management.

Custodian also supports running policies on infrastructure as code assets to provide feedback directly on developer workstations or within CI pipelines.

Custodian policies are written in simple YAML configuration files that enable users to specify policies on a resource type (EC2, ASG, Redshift, CosmosDB, PubSub Topic) and are constructed from a vocabulary of filters and actions.

It integrates with the cloud native serverless capabilities of each provider to provide for real time enforcement of policies with builtin provisioning. Or it can be run as a simple cron job on a server to execute against large existing fleets.



## Ref

