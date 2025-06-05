# Kubernetes Namespace Overview

## What is a Namespace?
A **Namespace** in Kubernetes is a logical partitioning mechanism that allows multiple teams or projects to share a cluster while keeping their resources isolated. It provides a way to scope resources and manage access control.

## Why Use Namespaces?
- **Resource Isolation:** Segregates workloads for different teams or environments (e.g., `dev`, `staging`, `prod`).
- **Access Control:** Enables Role-Based Access Control (RBAC) for fine-grained permissions.
- **Resource Quotas:** Helps in limiting resource usage per namespace.
- **Organization:** Structures cluster resources for better management.

## Default Namespaces
Kubernetes comes with a few pre-defined namespaces:
- **default:** Used when no namespace is specified.
- **kube-system:** Holds system-related components (e.g., CoreDNS, Kube Proxy).
- **kube-public:** Contains public resources accessible across the cluster.
- **kube-node-lease:** Stores node lease objects for node heartbeat tracking.

## Conclusion
Namespaces help in organizing and managing Kubernetes resources efficiently. They enable multi-tenancy and resource control within a single cluster.

