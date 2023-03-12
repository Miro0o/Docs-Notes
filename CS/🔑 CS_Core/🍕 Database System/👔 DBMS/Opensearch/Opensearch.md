# [Opensearch](https://opensearch.org)

[TOC]



## Res
📂 [Opensearch Docs](https://opensearch.org/docs/latest/)



## Intro
OpenSearch is a scalable, flexible, and extensible open-source software suite for search, analytics, and observability applications licensed under Apache 2.0. Powered by [Apache Lucene](https://lucene.apache.org/) and driven by the [OpenSearch Project community](https://opensearch.org/about.html), OpenSearch offers a vendor-agnostic toolset you can use to build secure, high-performance, cost-efficient applications. Use OpenSearch as an end-to-end solution or connect it with your preferred open-source tools or [partner projects](https://opensearch.org/partners).

### AWS Elasticsearch vs OpenSearch vs Open Distro for Elasticsearch (ODFE)

> 🔗 https://logit.io/blog/post/aws-elasticsearch-vs-opensearch/

With all of these terms coined in the wake of Elastic’s decision to make the ELK Stack closed-source, it can be very confusing to know the difference between the new distributions of Elasticsearch and Kibana being offered by Amazon Web Services and other cloud/Saas platforms.

**TL;DR**
AWS Elasticsearch Service (Amazon ES) referred to the proprietary service Amazon had offered since 2015, this solution offered managed Elasticsearch as a service.

Amazon OpenSearch Service is the successor to Amazon Elasticsearch Service and offers the latest version of OpenSearch as a managed solution. This news was announced on September 8th 2021.

Open Distro for Elasticsearch (ODFE) was the previous name for OpenSearch, on the official website for ODFE an announcement was made on June 25 2021 that all users should refer to the new OpenSearch site for news and updates as the previous site sporting the old branding will be selectively decommissioned in time.

OpenSearch and OpenSearch dashboards are the current rebrand of Open Distro for Elasticsearch which was also announced on September 8th, 2021. This is the latest fully open-source version of the Elastic Stack.

All of the terms above are directly connected to AWS’s involvement with the distribution of Elasticsearch and Kibana, with Logstash having been excluded from the development process.

#### Compatibility 
Most clients that work with Elasticsearch OSS 7.10.2 _should_ work with OpenSearch, but the latest versions of those clients might include license or version checks that artificially break compatibility. 

👀 Visit https://opensearch.org/docs/2.6/clients/index/



## Ref
