# Describe Cloud Concepts

The certification validates your basic knowledge of cloud services and how those services are provided with Azure.

## Describe Cloud Computing

This module introduces you to cloud computing. It covers things such as cloud concepts, deployment models, and understanding shared responsibility in the cloud.

### Introduction To Cloud Computing

In this module, you’ll be introduced to general cloud concepts. You’ll start with an introduction to the cloud in general. Then you'll dive into concepts like ***shared responsibility***, different ***cloud models***, and explore the ***unique pricing method*** for the cloud.

#### What is cloud computing?

***Cloud computing*** is the delivery of computing services ***over the internet***, it doesn’t have to be constrained by physical infrastructure the same way that a traditional datacenter is.

***Compute Power***: How much processing your computer can do.

***Storage***: How much data your computer can hold.

#### Describe The Shared Responsibility Model

> If you’re using a cloud SQL database, the cloud provider would be responsible for maintaining the actual database. However, you’re still responsible for the data that gets ingested into the database.

The shared responsibility model is heavily tied into the cloud service types: ***infrastructure*** as a service ***(IaaS)***, ***platform*** as a service ***(PaaS)***, and ***software*** as a service ***(SaaS)***.

***IaaS*** places the most responsibility on the consumer, with the cloud provider being responsible for the basics of ***physical security, power, and connectivity***. On the other end of the spectrum, ***SaaS*** places most of the responsibility with the ***cloud provider***. ***PaaS***, being a ***middle ground*** between ***IaaS*** and ***SaaS***.

![Alt text](shared-responsibility-b3829bfe.svg)

### Define Cloud Models

The ***cloud models*** define the deployment type of cloud resources. The three main ***cloud models*** are: ***private, public, and hybrid***.

#### Private Cloud

***Private cloud*** provides much greater control for the company and its IT department. However, it also comes with ***greater cost*** and fewer of the benefits of a public cloud deployment.

#### Public Cloud

A ***public cloud*** is built, controlled, and maintained by a ***third-party cloud provider***. With a public cloud, anyone that wants to purchase cloud services can access and use resources.

#### Hybrid Cloud

A hybrid cloud environment can be used to ***allow a private cloud*** to surge for increased, temporary demand by deploying ***public cloud resources***.

#### Multi-cloud

In a ***multi-cloud*** scenario, you use ***multiple*** public cloud providers. Maybe you use different features from different ***cloud providers***. Or maybe you started your cloud journey with one provider and are in the ***process of migrating*** to a different provider.

#### Azure Arc

***Azure Arc*** can help manage your ***cloud environment***, whether it's a ***public cloud*** solely on Azure, a ***private cloud*** in your datacenter, a ***hybrid configuration***, or even a ***multi-cloud environment*** running on multiple cloud providers at once.

#### Azure VMware Solution

***Azure VMware*** Solution lets you run your VMware workloads in Azure with seamless integration and scalability.

### Describe The Consumption-Based Model

***Capital expenditure (CapEx)*** is typically a ***one-time***, up-front expenditure to purchase or secure tangible resources. In contrast, ***operational expenditure (OpEx)*** is spending money on services or products ***over time***.

***Cloud computing*** falls under ***OpEx*** because cloud computing operates on a ***consumption-based model***. Instead, ***you pay for the IT resources you use***.

#### Compare Cloud Pricing Models

***Cloud computing*** is the delivery of computing services over the internet by using a ***pay-as-you-go pricing model***.

- ***Plan and manage*** your operating ***costs***.
- ***Run*** your infrastructure ***more efficiently***.
- ***Scale*** as your business ***needs change***.

Instead of maintaining CPUs and storage in your datacenter, you rent them for the time that you need them.

## Describe The Benefits Of Using Cloud Services

This module introduces you to the benefits ***cloud computing*** can offer you or your organization.

### Describe The Benefits Of High Availability And Scalability In The Cloud

When building or deploying a cloud application, two of the biggest considerations are ***uptime (or availability)*** and the ability to ***handle demand (or scale)***.

#### High Availability

***High availability*** focuses on ensuring ***maximum availability***, regardless of disruptions or events that may occur.

***Service Level Agreements (SLAs)*** are a key component of ***high availability***. An SLA is a ***contract between a service provider and a customer*** that defines the level of service expected from the service provider.

#### Scalability

***Scalability*** refers to the ***ability to adjust resources*** to meet demand.

***Scaling*** generally comes in two varieties: ***vertical and horizontal***.

- ***Vertical scaling*** means increasing or decreasing the ***size*** of a ***virtual machine***.

- ***Horizontal scaling*** means increasing or decreasing the ***number of virtual machines***.

### Describe The Benefits Of Reliability And Predictable In The Cloud

***Reliability and predictability*** are two crucial cloud benefits that help you develop solutions with confidence.

#### Reliability

***Reliability*** is the ability of a system to ***recover from failures*** and ***continue to function***.

With a decentralized design, the cloud enables you to have resources deployed in regions around the world. With this global scale, even if one region has a catastrophic event other regions are still up and running.

#### Predictability

***Predictability*** can be focused on ***performance predictability*** or ***cost predictability***.

#### Performance

***Performance predictability*** focuses on predicting the ***resources needed*** to deliver a ***positive experience*** for your customers.

***Autoscaling, load balancing, and high availability*** are just some of the cloud concepts that support performance predictability.

#### Cost

***Cost predictability*** is focused on predicting or forecasting the ***cost of the cloud spend***.

By operating in the cloud and using cloud analytics and information, you can predict future costs and adjust your resources as needed.

### Describe The Benefits Of Security And Governance In The Cloud

***Cloud-based auditing*** helps flag any resource that’s out of compliance with your corporate standards and provides mitigation strategies.

If you want ***maximum control*** of security, ***infrastructure as a service*** provides you with physical resources but lets you manage the ***operating systems*** and ***installed software***, including patches and maintenance. If you want patches and maintenance taken care of automatically, ***platform as a service or software as a service*** deployments may be the best cloud strategies for you.

#### Describe The Benefits Of Manageability In The Cloud

A major benefit of ***cloud computing*** is the ***manageability*** options.

### Management Of The Cloud

***Management of the cloud*** speaks to managing your ***cloud resources***.

- ***Automatically scale*** resource deployment based on need.
- Deploy resources based on a ***pre-configured template***, removing the need for manual configuration.
- ***Monitor*** the health of resources and automatically replace failing resources.
- ***Receive automatic alerts*** based on configured metrics, so you’re aware of performance in real time.

#### Management In The Cloud

***Management in the cloud*** speaks to ***how you’re able to manage*** your cloud environment and resources.

- Through a ***web portal***.
- Using a ***command line interface (CLI)***.
- Using ***APIs***.
- Using ***PowerShell***.

## Describe Cloud Service Type

This module covers the different ***cloud service types*** and shares some of the use cases and benefits aligned with each service type.

### Describe Infrastructure As A Service (IaaS)

With ***IaaS***, you’re essentially ***renting the hardware in a cloud datacenter***, but what you do with that hardware is ***up to you***.

#### IaaS Shared Responsibility Model

The ***cloud provider*** is responsible for ***maintaining the physical infrastructure and its access to the internet***.
You’re responsible for ***installation and configuration, patching and updates, and security***.

#### IaaS Scenarios

- ***Lift-and-shift migration***: You’re standing up cloud resources similar to your on-prem datacenter, and then simply moving the things running on-prem to running on the IaaS infrastructure.
- ***Testing and development***: You have established configurations for development and test environments that you need to rapidly replicate.

### Describe Platform As A Service (PaaS)

***Platform as a service (PaaS)*** is a ***middle ground*** between renting space in a datacenter (***infrastructure as a service***) and paying for a complete and deployed solution (***software as a service***).

#### PaaS Shared Responsibility Model

The ***cloud provider*** is responsible for ***maintaining the physical infrastructure and its access to the internet***, just like in IaaS. In the PaaS model, the cloud provider will also ***maintain the operating systems, databases, and development tools***.

#### PaaS Scenarios

- ***Development framework***: PaaS provides a framework that developers can build upon to develop or customize cloud-based applications.
- ***Analytics or business intelligence***: Tools provided as a service with PaaS allow organizations to analyze and mine their data, finding insights and patterns and predicting outcomes to improve forecasting, product design decisions, investment returns, and other business decisions.

### Describe Software As A Service (SaaS)

***Software as a service (SaaS)*** is the most complete cloud service model from a product perspective. With ***SaaS***, you’re essentially ***renting or using a fully developed application***.

#### SaaS Shared Responsibility Model

In a SaaS environment you’re responsible for the ***data that you put into the system, the devices that you allow to connect to the system, and the users that have access***.

The cloud provider is responsible for ***physical security of the datacenters, power, network connectivity, and application development and patching***.

#### SaaS Scenarios

- ***Email*** and ***messaging***.
- ***Business productivity applications***.
- ***Finance*** and ***expense*** tracking.
