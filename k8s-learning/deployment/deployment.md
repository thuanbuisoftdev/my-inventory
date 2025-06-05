# Kubernetes Deployment Overview

## What is a Deployment?
A **Deployment** is a higher-level resource in Kubernetes that manages **ReplicaSets and Pods**. It provides features like:
- **Automatic Pod scaling & replication**
- **Rolling updates & rollbacks**
- **Self-healing (restarts failed Pods)**
- **Declarative management (you define the desired state, Kubernetes maintains it)**

---

## Deployment vs. ReplicaSet vs. Pod
| Resource | Purpose |
|----------|---------|
| **Pod** | A single instance of a running containerized app. |
| **ReplicaSet** | Ensures a specified number of Pod replicas are running at all times. |
| **Deployment** | Manages ReplicaSets and allows updates, rollbacks, and scaling. |

---

## Deployment Lifecycle
1. **Create the Deployment** (`kubectl apply -f deployment.yaml`)
2. **Kubernetes creates a ReplicaSet**
3. **ReplicaSet creates and manages Pods**
4. If you update the Deployment, Kubernetes **creates a new ReplicaSet** and gradually replaces the old Pods.
5. If an issue occurs, you can **rollback** to a previous version.

---

## When to Use a Deployment?
- When you need **replicated** Pods  
- When you want **automatic updates & rollbacks**  
- When you want **self-healing & scaling**  


