
# 1. Zyxel Nebula

**Zyxel** is a Taiwan-based multinational organization that produces and sells network devices, eg access point, switch, gateway

In traditional approach, network administrators have to connect to each device directly to configure and monitor them.
These manually operations are inconvinence and time comsume, especially for enterpises own many devices.

**Zyxel Nebula** is a cloud-based network management platform that allows users to manage their devices via web and mobile apps.  

## Nebula system architecture

To ensure high scalability, availablity Nebula has combined many system architectures:

# Microservices architecture

Break the system into multiple services to allow development and deployment for each service independently
This help the system can easily adapt when market demands on each device types changed

- **Auth Service** – Manages authentication, authorization, and sessions.  
- **Per-Device-Type Services (AP service, SW service, GW service)** – These services handle configuration and monitoring for specficic device type. APIs designed to handle one device per request, so it is scalable.  
- **Management Service** – General configures multiple devices same time, call per-device-type service to provision settings.
- **Monitor Service** – General monitor and analyse data from multiple devices, call per-device-type to collect data.
- **License Service** – Manages licenses to use features on Nebula system and network device.  

# Distributed architecture

Distribute workloads to multiple servers to allow scaling with load balancing horizontally.

- **Service**: split service to 2 tiers: external tier server receive API request, internal tier server process request.
External tier service forward request to internal tier servers using Opentack RPC, this mechanism allow system to scale internal tier servers.
- **Job & Cronjob** – using distributed task queue(Celery) to distributes background tasks among worker servers, this mechanism allow system to scale worker servers.

# Event-Drive architecture

Use event publishing and subscription mechanism to communicate between components asynchronously

- **Backend** – Use Opentack notification library to let services communicate asynchrously.
- **Frontend** – Use reactive RxJS library to manage data, state and user events asynchronously.  

# Layered architecture

- **Backend**: layers: common library, cache, database, bussiness, API view
- **Frontend**: layers: common library, API, page(view, block, page)

Techology stack:

Backend:

- Language: Python 3
- Web framework: Flask, FastAPI
- Database: MongoDB
- Cache: Redis
- RPC: Openstack Olso messaging RPC
- Notification framework: Openstack Olso messaging notification
- Queue framework: Celery

Frontend:

- Framework: Angular
- CSS framework: Boostrap
