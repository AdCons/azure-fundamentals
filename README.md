# Azure Fundamentals AZ-900

## Learning Path 1: Describe Cloud Concepts

The certification validates your basic knowledge of cloud services and how those services are provided with Azure.

### Module 1: Describe Cloud Computing

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

### Module 2: Describe The Benefits Of Using Cloud Services

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

### Module 3: Describe Cloud Service Type

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

## Learning Path 2: Describe Azure Architecture And Services

This learning path explores Microsoft Azure, its architecture, and some of the most commonly used services and resources.

### Module 1: Describe The Core Architectural Components Of Azure

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

### Module 2: Describe Azure Compute And Networking Services

This module focuses on some of the ***computer*** services and ***networking*** services available within Azure.

#### Describe Azure Virtual Machines

An ***Azure VM*** gives you the ***flexibility of virtualization*** without having to buy and maintain the physical hardware that runs the ***VM***. However, as an ***IaaS offering***, you still need to configure, update, and maintain the software that runs on the ***VM***.

***VMs*** are an ideal choice when you need:

1. ***Total control*** over the operating system (OS).
2. The ability to run ***custom software***.
3. To use ***custom hosting*** configurations.

An image is a template used to create a ***VM*** and may already include an OS and other software, like development tools or web hosting environments.

##### Scale VMs In Azure

Azure can also manage the grouping of ***VMs*** for you with features such as ***scale sets and availability sets***.

##### Virtual Machine Scale Sets

Virtual machine ***scale sets*** let you create and manage a group of ***identical, load-balanced VMs***. Scale sets allow you to centrally ***manage, configure, and update*** a large number of VMs in minutes.

***Virtual machine scale sets*** also automatically deploy a ***load balancer*** to make sure that your resources are being used efficiently.

##### Virtual Machine Availability Sets

***Availability sets*** are designed to ensure that ***VMs stagger*** updates and have varied power and network connectivity, ***preventing*** you from losing all your ***VMs*** with a single network or power failure.

1. ***Update domain***: Groups ***VMs*** that can be ***rebooted*** at the same time.
2. ***Fault domain***: Groups your ***VMs*** by ***common*** power source and network switch.

Best of all, there’s ***no additional cost*** for configuring an ***availability set***. You only pay for the VM instances you create.

##### Examples Of When To Use VMs

Some common examples or use cases for virtual machines include:

1. ***Testing*** and ***development***.
2. Running ***applications*** in the ***cloud***.
3. Extending your ***datacenter*** to the ***cloud***.
4. ***Disaster recovery***.

##### Move To The Cloud With VMs

VMs are also an excellent choice when you ***move*** from a ***physical*** server to the ***cloud*** (also known as ***lift and shift***). You can create an ***image*** of the physical server and ***host it*** within a VM with little or ***no changes***.

##### VM Resources

1. ***Size***: Purpose, number of processor cores, and amount of RAM.
2. ***Storage disks***: Hard disk drives, solid state drives, etc.
3. ***Networking***: Virtual network, public IP address, and port configuration.

#### Describe Azure Containers

***Containers*** are a ***virtualization environment***. Unlike ***virtual machines***, you don't manage the ***operating system*** for a container.

##### Azure Container Instances

***Azure Container Instances*** allow you to upload your ***containers*** and then the service will ***run*** the containers for you. ***Azure Container Instances*** are a ***platform as a service (PaaS)*** offering.

##### Use Containers In Your Solutions

***Containers*** are often used to create solutions by using a ***microservice architecture***. This architecture is where you ***break solutions*** into ***smaller, independent*** pieces. This split allows you to separate ***portions of your app*** into ***logical*** sections that can be ***maintained, scaled, or updated independently***.

#### Describe Azure Functions

***Azure Functions*** is an ***event-driven, serverless*** compute option that doesn’t require maintaining virtual machines or containers. With ***Azure Functions***, an ***event wakes*** the function, alleviating the need to keep resources provisioned when there are no events.

##### Benefit Of Azure Functions

Using ***Azure Functions*** is ideal when you are ***not concerned*** about the underlying platform or infrastructure. Functions ***scale automatically*** based on demand.

***Functions*** are commonly used when you need to ***perform work*** in response to an ***event*** (often via a REST request), ***timer***, or ***message*** from another Azure service. ***Azure Functions*** runs your code when it's ***triggered*** and ***automatically deallocates*** resources when the function is finished.

Functions can be either ***stateless*** or ***stateful***:

1. ***Stateless (default)***: They ***behave*** as if they're ***restarted*** every time they respond to an event.
2. ***Stateful (called Durable Functions)***: A context is ***passed through*** the function to track ***prior activity***.

***Functions*** are a ***key*** component of ***serverless computing***. This ***flexibility*** allows you to manage scaling, run on virtual networks, and even completely isolate the functions.

#### Describe Application Hosting Options

If you need to host your application on Azure, you might initially turn to a virtual machine (VM) or containers.

##### Azure App Service

***App Service*** enables you to build and host ***web apps, background jobs, mobile back-ends, and RESTful APIs*** in the programming language of your choice without managing infrastructure.

***Azure App Service*** lets you focus on ***building*** and ***maintaining*** your app, and Azure focuses on keeping the environment up and running.

##### Types Of Apps Services

With App Service, you can host most common app service styles like:

1. ***Web apps***: Used for hosting websites and web applications.
2. ***API apps***: Used for hosting RESTful APIs.
3. ***WebJobs***: Used for running a program or script in the ***same context*** as a web app, API app, or mobile app.
4. ***Mobile apps***: Used for hosting mobile app back-ends.

***App Service*** handles most of the infrastructure decisions you deal with in hosting web-accessible apps:

1. ***Deployment and management*** are integrated into the platform.
2. ***Endpoints*** can be secured.
3. ***Sites*** can be ***scaled*** quickly to handle high traffic loads.
4. The ***built-in load balancing and traffic manager*** provide high availability.

All of these app styles are hosted in the same infrastructure and share these benefits. This flexibility makes App Service the ideal choice to host web-oriented applications.

#### Describe Azure Virtual Networking

You can think of an ***Azure network*** as an extension of your on-premises network with resources that link other ***Azure resources***.

***Azure virtual networks*** provide the following ***key*** networking capabilities:

1. ***Isolation*** and ***segmentation***: The ***IP*** range only exists within the virtual network and isn't internet routable.
2. ***Internet communications***: You can ***enable*** incoming connections from the internet.
3. ***Communicate between Azure resources***: Virtual networks can connect not only ***VMs*** but other ***Azure resources***.
4. ***Communicate with on-premises resources***:
    - ***Point-to-site*** virtual private network connections are from a computer outside your organization back into your corporate network.
    - ***Site-to-site*** virtual private networks link your on-premises VPN device or gateway to the Azure VPN gateway in a virtual network.
    - ***Azure ExpressRoute*** provides a dedicated private connectivity to Azure that doesn't travel over the internet.
5. ***Route network traffic***:
    - ***Route tables*** allow you to define rules about ***how*** traffic should be directed.
    - ***Border Gateway Protocol (BGP)***: Routing protocol that allows you to exchange routes between your on-premises network and Azure.
6. ***Filter network traffic***:
    - ***Network security groups*** are Azure resources that can contain multiple inbound and outbound security rules.
    - A ***network virtual appliance*** carries out a particular network function, such as running a ***firewall*** or performing ***wide area network (WAN)*** optimization.
7. ***Connect virtual networks***:
    - Network traffic between ***peered networks*** is private, and travels on the Microsoft backbone network, ***never*** entering the public internet.
    - ***User-defined routes (UDR)*** allow you to control the routing tables between subnets within a virtual network or between virtual networks.

***Azure virtual networking*** supports both ***public and private*** endpoints to enable communication between external or internal resources with other internal resources:

1. ***Public endpoints***: Have a public IP address and can be accessed from ***anywhere*** in the world.
2. ***Private endpoints***: Exist within a ***virtual network*** and have a ***private IP*** address from within the address space of that virtual network.

#### Describe Azure Virtual Private Networks

***VPNs*** are typically deployed to connect two or more ***trusted*** private networks to one another ***over an untrusted network*** (typically the ***public internet***). ***VPNs*** can enable networks to safely and securely share ***sensitive information***.

##### VPN Gateway

A ***VPN gateway*** is a type of virtual network gateway.

1. Connect ***on-premises datacenters to virtual networks*** through a ***site-to-site*** connection.
2. Connect ***individual devices to virtual networks*** through a ***point-to-site*** connection.
3. Connect ***virtual networks to other virtual networks*** through a ***network-to-network*** connection.

> All data transfer is ***encrypted*** inside a private tunnel as it crosses the internet.

When you deploy a VPN gateway, you specify the VPN type: either ***policy-based or route-based***.

1. ***Policy-based VPN gateways***: Specify statically the ***IP address*** of packets that should be ***encrypted*** through each tunnel.
2. ***Route-based gateways***: ***IPSec tunnels*** are modeled as a network interface or virtual tunnel interface.

Use a ***route-based VPN gateway*** if you need any of the following types of connectivity:

1. Connections ***between*** virtual networks
2. ***Point-to-site*** connections
3. ***Multisite*** connections
4. ***Coexistence*** with an ***Azure ExpressRoute*** gateway

##### High-availability scenarios

There are a few ways to maximize the ***resiliency*** of your VPN gateway.

1. ***Active/standby***: When planned maintenance or unplanned disruption ***affects*** the active instance, the ***standby*** instance ***automatically*** assumes ***responsibility*** for connections without any user intervention.
2. ***Active/active***: In this configuration, you assign a ***unique public IP address*** to each instance. You then create ***separate tunnels*** from the on-premises device to each IP address.
3. ***ExpressRoute Failover***: In high-availability scenarios, where there's risk associated with an outage of an ***ExpressRoute circuit***, you can also provision a ***VPN gateway*** that uses the ***internet*** as an ***alternative*** method of connectivity.
4. ***Zone Redundant Gateways***: Deploying gateways in ***Azure availability zones*** physically and logically separates gateways within a region while protecting your on-premises network connectivity to Azure from zone-level failures.

#### Describe Azure ExpressRoute

***Azure ExpressRoute*** lets you extend your on-premises networks into the Microsoft cloud over a private connection, with the help of a connectivity provider.

***Connectivity*** can be from an ***any-to-any (IP VPN) network***, a ***point-to-point Ethernet network***, or a ***virtual cross-connection*** through a connectivity provider at a colocation facility.

***ExpressRoute*** connections ***don't*** go over the ***public Internet***. This allows ***ExpressRoute*** connections to offer more ***reliability, faster speeds, consistent latencies, and higher security*** than typical connections over the Internet.

##### Features And Benefits Of ExpressRoute

There are several benefits to using ***ExpressRoute*** as the connection service between Azure and on-premises networks.

1. Connectivity to Microsoft ***cloud services*** across ***all regions*** in the geopolitical region.
    - Microsoft ***Office 365***
    - Microsoft ***Dynamics 365***
    - ***Azure compute services***, such as Azure Virtual Machines
    - ***Azure cloud services***, such as Azure Cosmos DB and Azure Storage
2. ***Global connectivity*** to Microsoft services across all regions with the ***ExpressRoute Global Reach***.
    - You can enable ***ExpressRoute Global Reach*** to exchange data across your on-premises sites by connecting your ***ExpressRoute circuits***.
3. ***Dynamic routing*** between your network and Microsoft via ***Border Gateway Protocol (BGP)***.
    - This protocol enables ***dynamic routing*** between your ***on-premises network*** and ***services*** running in the Microsoft cloud.
4. Built-in ***redundancy*** in every peering location for ***higher reliability***.
    - Each connectivity provider uses redundant devices to ensure that connections established with Microsoft are highly available.

##### ExpressRoute Connectivity Models

***ExpressRoute*** supports four models that you can use to connect your on-premises network to the Microsoft cloud:

1. ***CloudExchange colocation***: Co-location refers to your datacenter, office, or other facility being physically co-located at a cloud exchange, such as an ISP.
2. ***Point-to-point Ethernet connection***: Refers to using a ***point-to-point*** connection to connect your facility to the Microsoft cloud.
3. ***Any-to-any connection***: You can integrate your ***wide area network (WAN)*** with Azure by providing connections to your offices and datacenters.
4. ***Directly from ExpressRoute sites***: ***ExpressRoute Direct*** provides dual 100 Gbps or 10-Gbps connectivity, which supports ***Active/Active*** connectivity at scale.

#### Describe Azure DNS

***Azure DNS*** is a hosting service for ***DNS domains*** that provides ***name resolution*** by using Microsoft Azure infrastructure.

##### Benefit Of Azure DNS

***Azure DNS*** leverages the scope and scale of Microsoft Azure to provide numerous benefits, including:

1. ***Reliability and performance***:
    - Azure DNS uses anycast networking, so each DNS query is answered by the closest available DNS server to provide fast performance and high availability for your domain.
2. ***Security***:
    - ***Azure role-based access control (Azure RBAC)*** to control who has access to specific actions for your organization.
    - ***Activity logs*** to monitor how a user in your organization modified a resource or to find an error when troubleshooting.
    - ***Resource locking*** to lock a subscription, resource group, or resource. Locking prevents other users in your organization from accidentally deleting or modifying critical resources.
3. ***Ease of Use***
    - Because Azure DNS is running on Azure, it means you can manage your domains and records with the Azure portal, Azure PowerShell cmdlets, and the cross-platform Azure CLI.
4. ***Customizable virtual networks***
    - ***Azure DNS*** also supports private DNS domains. This feature allows you to use your ***own custom domain names*** in your private virtual networks, rather than being stuck with the Azure-provided names.
5. ***Alias records***
    - If the ***IP address*** of the underlying resource changes, the ***alias record set*** seamlessly ***updates itself*** during DNS resolution. The ***alias record set*** points to the service instance, and the service instance is associated with an ***IP address***.

### Module 3: Describe Azure Storage Services

This module introduces you to ***storage*** in Azure, including things such as different types of storage and how a ***distributed*** infrastructure can make your data more ***resilient***.

#### Describe Data Storage Accounts

A ***storage account*** provides a unique namespace for your Azure Storage data that's accessible from ***anywhere*** in the world over HTTP or HTTPS.

In order to do this, every ***storage account*** in Azure must have a ***unique-in-Azure*** account name. The ***combination*** of the ***account name*** and the Azure Storage ***service endpoint*** forms the endpoints for your storage account.

#### Describe Azure Storage Redundancy

***Redundancy*** ensures that your storage account meets its ***availability*** and ***durability*** targets even in the face of failures.

The factors that help determine which redundancy option you should choose include:

1. How your data is ***replicated*** in the ***primary region***.
2. Whether your data is ***replicated*** to a ***second region*** that is ***geographically distant*** to the ***primary region***, to protect against regional disasters.
3. Whether your application requires ***read access*** to the replicated data in the ***secondary region*** if the primary region becomes ***unavailable***.

##### Redundancy In The Primary Region

***Data*** in an Azure Storage account is ***always replicated three times*** in the ***primary region***.

- ***Locally Redundant Storage (LRS)***: Replicates your data ***three times*** within a single data center in the ***primary region***. ***LRS*** is the ***lowest-cost redundancy*** option and offers the least durability compared to other options. ***(11 nines)***

![Alt text](locally-redundant-storage-37247957.png)

- ***Zone Redundant Storage (ZRS)***: Replicates your Azure Storage data ***synchronously*** across ***three Azure availability zones*** in the ***primary region***. With ZRS, your data is still accessible for both ***read and write*** operations even if a zone becomes unavailable. ***(12 nines)***

![Alt text](zone-redundant-storage-6dd46d22.png)

##### Redundancy In A Secondary Region

When you create a ***storage account***, you select the ***primary region*** for the account. The ***paired secondary region*** is based on Azure Region Pairs, and ***can't be changed***.

- ***Recovery Point Objective (RPO)***: The RPO indicates the ***point in time*** to which data can be ***recovered***.

- ***Geo-redundant Storage***: It then ***copies*** your data ***three times asynchronously*** to a single physical location in the ***secondary region*** (the region pair) using ***LRS***. ***(16 nines)***

![Alt text](geo-redundant-storage-3432d558.png)

- ***Geo-zone-redundant Storage***: Data in a GZRS storage account is ***copied*** across ***three Azure availability zones*** in the ***primary region*** (similar to ZRS) and is also ***replicated*** to a ***secondary*** geographic region, using ***LRS***, for protection from regional disasters. ***(16 nines)***

![Alt text](geo-zone-redundant-storage-138ab5af.png)

If you enable ***read access*** to the ***secondary region***, your data is ***always*** available, even when the ***primary region*** is ***running optimally***.

#### Describe Azure Storage Services

The Azure Storage platform includes the following data services:

1. ***Azure Blobs***
    - A ***massively scalable*** object store for ***text*** and ***binary data***.
    - ***Unstructured***, meaning that there are no restrictions on the kinds of data it can hold.
    - Blobs ***aren't*** limited to ***common file formats***.
    - Objects in Blob storage can be ***accessed*** from anywhere in the world via ***HTTP or HTTPS***.
    - Blob storage is ideal for:
        1. Serving ***images*** or ***documents*** directly to a ***browser***.
        2. Storing ***files*** for ***distributed access***.
        3. ***Streaming*** video and audio.
        4. Storing data for ***backup and restore***, disaster recovery, and archiving.
        5. Storing data for ***analysis*** by an on-premises or Azure-hosted service.
2. ***Azure Files***
    - Azure Files offers ***fully managed*** file shares in the cloud.
    - Azure Files key ***benefits***:
        1. ***Shared access***: Azure file shares support the industry standard ***Server Message Block (SMB)*** and ***Network File System (NFS)*** protocols.
        2. ***Fully managed***: Azure file ***shares*** can be created without the need to manage ***hardware or an OS***.
        3. ***Scripting and tooling***: ***PowerShell*** cmdlets and Azure CLI can be used to ***create, mount, and manage*** Azure file shares as part of the administration of Azure applications.
        4. ***Resiliency***: Azure Files has been ***built*** from the ground up to ***always be available***.
        5. ***Familiar programmability***: ***Applications*** running in Azure can ***access data*** in the share via file system ***I/O APIs***.
3. ***Azure Queues***
    - A ***messaging*** store for reliable messaging between application components.
    - Each individual message can be up to ***64 KB*** in size.
    - ***Queues*** are commonly used to create a ***backlog*** of work to process ***asynchronously***.
    - ***Queue*** storage can be combined with ***compute functions*** like Azure Functions to take an ***action*** when a ***message*** is received.
4. ***Azure Disks***
    - ***Block-level*** storage volumes for ***Azure VMs***.
    - They’re the same as a ***physical disk***, but they’re ***virtualized***

Data stored in the cloud can be handled differently based on ***how it's generated, processed, and accessed*** over its lifetime.

1. ***Hot access tier***: Optimized for storing data that is ***accessed frequently*** (for example, images for your website).
    - Can be set at the ***account level***.
    - Can be set at the ***blob level***, during or after upload.
2. ***Cool access tier***: Optimized for data that is ***infrequently accessed*** and stored for ***at least 30 days*** (for example, invoices for your customers).
    - Can be set at the ***account level***.
    - Can be set at the ***blob level***., during or after upload.
    - Requires high durability, retrieval latency, and throughput ***characteristics similar to hot data***.
    - Slightly ***lower*** availability service-level agreement ***(SLA)*** and ***higher access costs***.
3. ***Archive access tier***: Appropriate for data that is ***rarely accessed*** and stored for ***at least 180 days***, with flexible latency requirements (for example, long-term backups).
    - ***Isn't*** available at the ***account level***.
    - Can be set at the ***blob level***, during or after upload.
    - Offers the ***lowest storage costs***, but also the ***highest costs to access*** data.

##### Benefits Of Azure Storage

Azure Storage services offer the following benefits for application developers and IT professionals:

1. ***Durable and highly available***: Redundancy ensures that your data is safe if transient hardware failures occur.
2. ***Secure***: All data written to an Azure storage account is encrypted by the service.
3. ***Managed***: Azure handles hardware maintenance, updates, and critical issues for you.
4. ***Accessible***: Data in Azure Storage is accessible from anywhere in the world over HTTP or HTTPS.

#### Identify Azure Data Migration Options

Azure supports both ***real-time migration*** of infrastructure, applications, and data using ***Azure Migrate*** as well as ***asynchronous migration*** of data using ***Azure Data Box***.

##### Azure Migrate

***Azure Migrate*** is a service that helps you migrate from an on-premises environment to the cloud. It provides the following:

1. ***Unified migration platform***: A single portal to start, run, and track your migration to Azure.
2. ***Range of tools***: A range of tools for assessment and migration.
3. ***Assessment and migration***: In the ***Azure Migrate hub***, you can assess and migrate your on-premises infrastructure to Azure.

***Azure Migrate hub*** also includes the following tools to help with migration:

1. ***Azure Migrate, Discovery and assessment***: Discover and assess on-premises servers running on VMware, Hyper-V, and physical servers in ***preparation for migration*** to Azure.
2. ***Azure Migrate, Server Migration***: Migrate VMware VMs, Hyper-V VMs, physical servers, other virtualized servers, and public cloud VMs ***to Azure***.
3. ***Data Migration Assistant***: Stand-alone tool to assess SQL Servers. It helps pinpoint potential problems blocking migration.
4. ***Azure Database Migration Service***: Migrate on-premises ***databases*** to Azure VMs running SQL Server, Azure SQL Database, or SQL Managed Instances.
5. ***Web app migration assistant***: Standalone tool to assess on-premises ***websites*** for migration to ***Azure App Service***.
6. ***Azure Data Box***: Use Azure Data Box products to move ***large amounts of offline data*** to Azure.

##### Azure Data Box

The ***secure data transfer*** is accelerated by shipping you a proprietary ***Data Box storage device*** that has a maximum usable storage capacity of ***80 terabytes***. Data Box is ***ideally suited*** to transfer data sizes ***larger than 40 TBs*** in scenarios with no to limited network connectivity.

Here are the various scenarios where ***Data Box*** can be used to ***import*** data to Azure.

1. ***Onetime migration*** - when a *large amount of on-premises data is moved to Azure.
2. Moving a media library from ***offline tapes*** into Azure to create an ***online media library***.
3. Migrating your ***VM farm, SQL server, and applications*** to Azure.
4. Moving ***historical data*** to Azure for in-depth ***analysis and reporting*** using ***HDInsight***.
5. ***Initial bulk transfer*** - when an initial bulk transfer is done using Data Box ***(seed)*** followed by ***incremental transfers*** over the network.
6. ***Periodic uploads*** - when large amount of data is generated periodically and needs to be moved to Azure.

Here are the various scenarios where Data Box can be used to export data from Azure.

1. ***Disaster recovery*** - in a typical disaster recovery scenario, a large amount of Azure data is exported to a Data Box.
2. ***Security requirements*** - when you need to be able to export data out of Azure due to ***government*** or ***security requirements***.
3. ***Migrate back to on-premises or to another cloud service provider*** - when you want to move all the data back to on-premises, or to another cloud service provider, export data via Data Box to migrate the workloads.

#### Identify Azure File Movement Options

In addition to ***large scale migration*** using services like Azure Migrate and Azure Data Box, Azure also has ***tools*** designed to help you move or interact with ***individual files or small file groups***.

##### AzCopy

With ***AzCopy***, you can ***upload*** files, ***download*** files, ***copy*** files ***between storage accounts***, and even ***synchronize (one direction)*** files. ***AzCopy*** can even be configured to ***work with other cloud providers*** to help move files back and forth between clouds.

##### Azure Storage Explorer

***Azure Storage Explorer*** is a standalone app that provides a ***graphical interface*** to manage ***files and blobs*** in your Azure Storage Account.

##### Azure File Sync

***Azure File Sync*** is a tool that lets you ***centralize*** your file shares in Azure Files and keep the ***flexibility, performance, and compatibility*** of a ***Windows file server***.

With ***Azure File Sync***, you can:

1. Use ***any protocol*** that's available on ***Windows Server*** to access your data locally, including ***SMB, NFS, and FTPS***.
2. Have as many ***caches as you need*** across the world.
3. ***Replace a failed local server*** by installing Azure File Sync on a new server in the same datacenter.
4. Configure ***cloud tiering*** so the most ***frequently*** accessed files are replicated ***locally***, while ***infrequently*** accessed files are kept in the ***cloud until requested***.

### Module 4: Describe Azure Identity, Access And Security Services

This module covers some of the authorization and authentication methods available with Azure.
