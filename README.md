# Azure Fundamentals AZ-900

## Describe Cloud Concepts

The certification validates your basic knowledge of cloud services and how those services are provided with Azure.

### Describe Cloud Computing

This module introduces you to cloud computing. It covers things such as cloud concepts, deployment models, and understanding shared responsibility in the cloud.

#### Introduction To Cloud Computing

You'll dive into concepts like ***shared responsibility***, different ***cloud models***, and explore the ***unique pricing method*** for the cloud.

##### What is cloud computing?

***Cloud computing*** is the delivery of computing services ***over the internet***, it doesn’t have to be constrained by physical infrastructure the same way that a traditional datacenter is.

1. ***Compute Power***: How much processing your computer can do.
2. ***Storage***: How much data your computer can hold.

##### Describe The Shared Responsibility Model

The shared responsibility model is heavily tied into the cloud service types: ***infrastructure*** as a service ***(IaaS)***, ***platform*** as a service ***(PaaS)***, and ***software*** as a service ***(SaaS)***.

1. ***IaaS*** places the most responsibility on the consumer, with the cloud provider being responsible for the basics of ***physical security, power, and connectivity***.
2. ***SaaS*** places most of the responsibility with the ***cloud provider***.
3. ***PaaS***, being a ***middle ground*** between ***IaaS*** and ***SaaS***.

![Alt text](shared-responsibility-b3829bfe.svg)

#### Define Cloud Models

The ***cloud models*** define the deployment type of cloud resources. The three main ***cloud models*** are:

1. ***private***
2. ***public***
3. ***hybrid***

##### Private Cloud

***Private cloud*** provides much greater control for the company and its IT department. However, it also comes with ***greater cost*** and ***fewer*** of the benefits of a public cloud deployment.

##### Public Cloud

A ***public cloud*** is built, controlled, and maintained by a ***third-party cloud provider***. With a public cloud, anyone that wants to purchase cloud services can access and use resources.

##### Hybrid Cloud

A hybrid cloud environment can be used to ***allow a private cloud*** to surge for increased, temporary demand by deploying ***public cloud resources***.

##### Multi-cloud

In a ***multi-cloud*** scenario, you use ***multiple*** public cloud providers. Maybe you use different features from different ***cloud providers***. Or maybe you started your cloud journey with one provider and are in the ***process of migrating*** to a different provider.

##### Azure Arc

***Azure Arc*** can help manage your ***cloud environment***, whether it's a ***public cloud*** solely on Azure, a ***private cloud*** in your datacenter, a ***hybrid configuration***, or even a ***multi-cloud environment*** running on multiple cloud providers at once.

##### Azure VMware Solution

***Azure VMware*** Solution lets you run your VMware workloads in Azure with seamless ***integration and scalability***.

#### Describe The Consumption-Based Model

***Capital expenditure (CapEx)*** is typically a ***one-time***, up-front expenditure to purchase or secure tangible resources. In contrast, ***operational expenditure (OpEx)*** is spending money on services or products ***over time***.

***Cloud computing*** falls under ***OpEx*** because cloud computing operates on a ***consumption-based model***. Instead, ***you pay for the IT resources you use***.

##### Compare Cloud Pricing Models

***Cloud computing*** is the delivery of computing services over the internet by using a ***pay-as-you-go pricing model***.

- ***Plan and manage*** your operating ***costs***.
- ***Run*** your infrastructure ***more efficiently***.
- ***Scale*** as your business ***needs change***.

Instead of maintaining CPUs and storage in your datacenter, you rent them for the time that you need them.

### Describe The Benefits Of Using Cloud Services

This module introduces you to the benefits ***cloud computing*** can offer you or your organization.

#### Describe The Benefits Of High Availability And Scalability In The Cloud

When building or deploying a cloud application, two of the biggest considerations are ***uptime (or availability)*** and the ability to ***handle demand (or scale)***.

##### High Availability

***High availability*** focuses on ensuring ***maximum availability***, regardless of disruptions or events that may occur.

***Service Level Agreements (SLAs)*** are a key component of ***high availability***. An SLA is a ***contract between a service provider and a customer*** that defines the level of service expected from the service provider.

##### Scalability

***Scalability*** refers to the ***ability to adjust resources*** to meet demand.

***Scaling*** generally comes in two varieties: ***vertical and horizontal***.

- ***Vertical scaling*** means increasing or decreasing the ***size*** of a ***virtual machine***.

- ***Horizontal scaling*** means increasing or decreasing the ***number of virtual machines***.

#### Describe The Benefits Of Reliability And Predictable In The Cloud

***Reliability and predictability*** are two crucial cloud benefits that help you develop solutions with confidence.

##### Reliability

***Reliability*** is the ability of a system to ***recover from failures*** and ***continue to function***.

With a decentralized design, the cloud enables you to have resources deployed in regions around the world.

##### Predictability

***Predictability*** can be focused on ***performance predictability*** or ***cost predictability***.

##### Performance

***Performance predictability*** focuses on predicting the ***resources needed*** to deliver a ***positive experience*** for your customers.

***Autoscaling, load balancing, and high availability*** are just some of the cloud concepts that support performance predictability.

##### Cost

***Cost predictability*** is focused on predicting or forecasting the ***cost of the cloud spend***.

By operating in the cloud and using cloud analytics and information, you can predict future costs and adjust your resources as needed.

#### Describe The Benefits Of Security And Governance In The Cloud

***Cloud-based auditing*** helps flag any resource that’s ***out*** of compliance with your corporate standards and provides mitigation strategies.

If you want ***maximum control*** of security, ***infrastructure as a service*** provides you with physical resources but lets you manage the ***operating systems*** and ***installed software***, including patches and maintenance.

If you want patches and maintenance taken care of automatically, ***platform as a service or software as a service*** deployments may be the best cloud strategies for you.

##### Describe The Benefits Of Manageability In The Cloud

A major benefit of ***cloud computing*** is the ***manageability*** options.

#### Management Of The Cloud

***Management of the cloud*** speaks to managing your ***cloud resources***.

- ***Automatically scale*** resource deployment based on need.
- Deploy resources based on a ***pre-configured template***, removing the need for manual configuration.
- ***Monitor*** the health of resources and automatically replace failing resources.
- ***Receive automatic alerts*** based on configured metrics, so you’re aware of performance in real time.

##### Management In The Cloud

***Management in the cloud*** speaks to ***how you’re able to manage*** your cloud environment and resources.

- Through a ***web portal***.
- Using a ***command line interface (CLI)***.
- Using ***APIs***.
- Using ***PowerShell***.

### Describe Cloud Service Type

This module covers the different ***cloud service types*** and shares some of the use cases and benefits aligned with each service type.

#### Describe Infrastructure As A Service (IaaS)

With ***IaaS***, you’re essentially ***renting the hardware in a cloud datacenter***, but what you do with that hardware is ***up to you***.

##### IaaS Shared Responsibility Model

The ***cloud provider*** is responsible for ***maintaining the physical infrastructure and its access to the internet***.
You’re responsible for ***installation and configuration, patching and updates, and security***.

##### IaaS Scenarios

- ***Lift-and-shift migration***: You’re standing up cloud resources similar to your on-prem datacenter, and then simply moving the things running on-prem to running on the IaaS infrastructure.
- ***Testing and development***: You have established configurations for development and test environments that you need to rapidly replicate.

#### Describe Platform As A Service (PaaS)

***Platform as a service (PaaS)*** is a ***middle ground*** between renting space in a datacenter (***infrastructure as a service***) and paying for a complete and deployed solution (***software as a service***).

##### PaaS Shared Responsibility Model

The ***cloud provider*** is responsible for ***maintaining the physical infrastructure and its access to the internet***, just like in IaaS. In the PaaS model, the cloud provider will also ***maintain the operating systems, databases, and development tools***.

##### PaaS Scenarios

- ***Development framework***: PaaS provides a framework that developers can build upon to develop or customize cloud-based applications.
- ***Analytics or business intelligence***: Tools provided as a service with PaaS allow organizations to analyze and mine their data, finding insights and patterns and predicting outcomes to improve forecasting, product design decisions, investment returns, and other business decisions.

#### Describe Software As A Service (SaaS)

***Software as a service (SaaS)*** is the most complete cloud service model from a product perspective. With ***SaaS***, you’re essentially ***renting or using a fully developed application***.

##### SaaS Shared Responsibility Model

In a SaaS environment you’re responsible for the ***data that you put into the system, the devices that you allow to connect to the system, and the users that have access***.

The cloud provider is responsible for ***physical security of the datacenters, power, network connectivity, and application development and patching***.

##### SaaS Scenarios

- ***Email*** and ***messaging***.
- ***Business productivity applications***.
- ***Finance*** and ***expense*** tracking.

## Describe Azure Architecture And Services

This learning path explores Microsoft Azure, its architecture, and some of the most commonly used services and resources.

### Describe The Core Architectural Components Of Azure

You'll learn about the ***physical infrastructure***, how resources are managed, and have a chance to create an ***Azure resource***.

#### What Is Azure?

Azure is a continually expanding set of cloud services that help you meet current and future business challenges.

##### What Does Azure Offer?

1. Continuous innovation
2. Commitment to open source
3. Hybrid Cloud Solutions
4. Security and Compliance

#### Get Started With Azure Accounts

1. To create and use ***Azure services***, you need an ***Azure subscription***.
2. After you've created an ***Azure account***, you're free to create additional subscriptions.
3. After you've created an ***Azure subscription***, you can start creating ***Azure resources*** within each subscription.

![Alt text](account-scope-levels-9ceb3abd.png)

#### Describe Azure Physical Infrastructure

The ***core*** architectural components of Azure may be broken down into two main groupings: the ***physical infrastructure***, and the ***management infrastructure***.

##### Physical Infrastructure

***Datacenters*** are facilities with ***resources*** arranged in racks, with dedicated ***power, cooling, and networking*** infrastructure.

1. ***Regions***: Geographical area on the planet that contains ***at least one***, but potentially multiple ***datacenters*** that are nearby and networked together with a ***low-latency*** network.
2. ***Availability zones***: Physically ***separate datacenters*** within an ***Azure region***. An ***availability zone*** is set up to be an isolation boundary. If one zone goes ***down***, the other continues ***working***.

![Alt text](availability-zones-c22f95a3.png)

Azure services that support availability zones fall into three categories:

1. ***Zonal services***: You pin the resource to a ***specific zone*** (for example, VMs, managed disks, IP addresses).
2. Zone-redundant services: The platform ***replicates*** automatically across zones (for example, zone-redundant storage, SQL Database).
3. ***Non-regional services***: Services are ***always available*** from Azure geographies and are ***resilient*** to zone-wide outages as well as region-wide outages.

##### Region Pairs

Because the ***pair of regions*** are directly connected and far enough apart to be isolated from regional disasters, you can use them to provide ***reliable services*** and ***data redundancy***.

![Alt text](region-pairs-7c495a33.png)

##### Sovereign Regions

***Sovereign regions*** are instances of Azure that are ***isolated*** from the main instance of Azure. You may need to use a sovereign region for ***compliance or legal*** purposes.

#### Describe Azure Management Infrastructure

The management infrastructure includes Azure resources and resource groups, subscriptions, and accounts.

##### Azure Resources And Resource Groups

A ***resource*** is the basic building block of Azure. ***Resource groups*** are simply groupings of resources. When you create a ***resource***, you’re required to place it into a ***resource group***.

![Alt text](resource-group-eb2d7177.png)

***Resource groups*** provide a convenient way to group resources together. When you ***apply*** an action to a ***resource group***, that action ***will apply*** to all the ***resources*** within the ***resource group***.

If you ***delete*** a ***resource group***, all the ***resources*** will be ***deleted***. If you ***grant or deny*** access to a ***resource group***, you’ve ***granted or denied*** access to all the ***resources*** within the ***resource group***.

##### Azure Subscriptions

Similar to how resource groups are a way to logically organize resources, ***subscriptions*** allow you to logically ***organize*** your ***resource groups*** and facilitate ***billing***.

![Alt text](subscriptions-d415577b.png)

In a ***multi-subscription*** account, you can use the subscriptions to configure different ***billing models*** and apply different ***access-management*** policies.

There are two types of subscription boundaries that you can use:

1. ***Billing boundary***: Azure generates separate billing reports and invoices for each subscription so that you can organize and manage costs.
2. ***Access control boundary***: Azure applies ***access-management policies*** at the ***subscription*** level, and you can create separate subscriptions to reflect different organizational structures.
3. ***Billing***: You can create additional subscriptions for ***billing*** purposes.

##### Create Additional Azure Subscriptions

1. ***Environments***: You can choose to create ***subscriptions*** to set up ***separate environments*** for development and testing, security, or to isolate data for compliance reasons.
2. ***Organizational structures***: You can create subscriptions to reflect different ***organizational structures***.

##### Azure Management Groups

You organize ***subscriptions*** into containers called ***management groups*** and ***apply*** governance conditions to the management groups.

***Management groups*** give you enterprise-grade management at a ***large scale***, no matter what type of subscriptions you might have. Management groups can be nested.

##### Management Group, Subscriptions, And Resource Group Hierarchy

You can build a ***flexible*** structure of ***management groups*** and subscriptions to organize your resources into a hierarchy for unified policy and access management.

![Alt text](management-groups-subscriptions-dfd5a108.png)

Some examples of how you could use management groups might be:

1. ***Create a hierarchy that applies a policy***: This policy will inherit onto all the ***subscriptions*** that are descendants of that ***management group*** and will ***apply*** to all VMs under those ***subscriptions***.
2. ***Provide user access to multiple subscriptions***: Assigning ***Azure RBAC*** at the management group level means that ***all*** sub-management groups, subscriptions, resource groups, and resources underneath that management group ***would also inherit*** those permissions.

Important facts about management groups:

1. ***10,000*** management groups can be supported in a ***single*** directory.
2. A ***management group tree*** can support up to ***six*** levels of ***depth***.
3. Each ***management group*** and ***subscription*** can support only ***one parent***.

### Describe Azure Compute And Networking Services

This module focuses on some of the computer services and networking services available within Azure.

### Describe Azure Storage Services

This module introduces you to storage in Azure, including things such as different types of storage and how a distributed infrastructure can make your data more resilient.

### Describe Azure Identity, Access And Security Services

This module covers some of the authorization and authentication methods available with Azure.
