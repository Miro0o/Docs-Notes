# Directory Services

[TOC]



## Res
↗ [Identity Access Management (IAM)](../../../CyberSecurity/🏰%20InfoSec/Access%20Control/Identity%20Access%20Management%20(IAM)/Identity%20Access%20Management%20(IAM).md)



## Intro
> 🔗 https://www.cyberark.com/what-is/directory-services/

A [directory service](https://www.cyberark.com/products/directory-services/) is a database for storing and maintaining information about users and resources. Directory Services are often referred to as directories, user stores, Identity Stores, or LDAP Directory, and they store information such as usernames, passwords, user preferences, information about devices, and more. Network and system administrators use directory services to onboard users, manage access privileges and monitor and control access to applications and infrastructure resources. For example, when a user accesses an application, that application will reference the directory service to ensure the user is legitimate and has the proper privileges to access and use that application.

Directory services are fundamental elements of an Identity Security strategy. Many [identity and access management (IAM)](https://www.cyberark.com/what-is/iam/) solutions use directory services in conjunction with [single sign-on](https://www.cyberark.com/what-is/sso/) (SSO), [multi-factor authentication](https://www.cyberark.com/what-is/mfa/) (MFA) or [identity lifecycle management](https://www.cyberark.com/what-is/identity-lifecycle-management/) functionality.


### Directory Services in the Cloud Era
Microsoft Active Directory is by far the most widely adopted directory service in the business world. Active Directory was conceived to maintain information about traditional enterprise IT implementations and risk boundaries. In a traditional IT environment, stationary office workers use company-owned devices to access resources and applications hosted in on-premises data centers.

Active Directory is not easily extended to the cloud-first, mobile-first era of IT where applications and users often reside outside the enterprise network perimeter. In today’s world, users access a variety of [SaaS](https://www.cyberark.com/what-is/saas/) solutions (e.g., Salesforce, Google Workspace), Infrastructure-as-a-Service (IaaS) workloads (e.g., virtual machines running on Microsoft Azure) and on-premises applications from any location, using any device (e.g., company-owned, BYOD, mobile, etc.).

![directory services](https://www.cyberark.com/wp-content/uploads/2021/11/directory-services-img-1.png)

Many businesses are implementing [virtual directories](https://www.cyberark.com/what-is/virtual-directory/) (sometimes called cloud directories) to support hybrid IT environments and cloud-centric users. A virtual directory aggregates and normalizes information from a variety of different on-premises directories (e.g., Active Directory, LDAP-based implementations) and cloud-based directories (e.g., Azure Active Directory, Google Cloud Directory)—in real-time. A virtual directory delivers a common framework and serves as an abstraction layer that decouples users and applications from the backend directory services for ultimate performance, scalability, and extensibility. Virtual directories also make it easy to securely manage [least privilege](https://www.cyberark.com/what-is/least-privilege/) access across hybrid implementations.

Enterprises can use virtual directories for peering and federation and to enable [single sign-on](https://www.cyberark.com/products/single-sign-on/) across different applications and services. Most virtual directories support modern authentication protocols like [SAML](https://www.cyberark.com/what-is/saml/), OpenID Connect, and OAuth, as well as traditional authentication protocols like Integrated Web Authentication (IWA).

Virtual directories are typically delivered as part of [IAM solutions](https://www.cyberark.com/products/access-management/) and can be deployed on-premises or in the cloud. In addition, leading [Identity-as-a-Service (IDaaS)](https://www.cyberark.com/what-is/idaas/) providers offer cloud-based virtual directories.


## Ref

