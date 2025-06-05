# Kubernetes Architecture Components

Kubernetes is a powerful container orchestration system designed to automate deployment, scaling, and operation of application containers. Its architecture is based on a master-worker model.

## 1. **Control Plane Components**

These components make global decisions about the cluster (e.g., scheduling), and detect and respond to cluster events.

### 1.1 **kube-apiserver**
- Serves the Kubernetes API using REST.
- Frontend of the Kubernetes control plane.
- All communication goes through the API server.

### 1.2 **etcd**
- Consistent and highly-available key-value store.
- Stores all cluster data (state and configuration).
- Acts as the source of truth for the cluster.

### 1.3 **kube-scheduler**
- Assigns workloads (pods) to nodes.
- Considers constraints like resource requirements, affinity/anti-affinity, taints, and tolerations.

### 1.4 **kube-controller-manager**
- Runs controller processes (e.g., Node Controller, Replication Controller).
- Ensures desired state of cluster resources.

### 1.5 **cloud-controller-manager**
- Integrates Kubernetes with cloud provider APIs.
- Manages cloud-specific controller logic (e.g., load balancers, volumes).

## 2. **Node Components**

These components run on every worker node and are responsible for running containers.

### 2.1 **kubelet**
- Primary node agent.
- Ensures containers are running in a Pod as expected.

### 2.2 **kube-proxy**
- Maintains network rules on nodes.
- Enables communication to/from Pods.
- Implements service abstraction.

### 2.3 **Container Runtime**
- Software that runs containers.
- Examples: Docker, containerd, CRI-O.

## 3. **Add-ons**

These are not part of the core but are commonly used.

### 3.1 **CoreDNS**
- Cluster DNS for service discovery.
- Resolves services within the cluster.

### 3.2 **Dashboard**
- Web-based UI for Kubernetes cluster management.

### 3.3 **Metrics Server**
- Collects resource usage data.
- Used for autoscaling and monitoring.

---

## Summary Diagram (Textual)

```text
Control Plane:
  - kube-apiserver
  - etcd
  - kube-scheduler
  - kube-controller-manager
  - cloud-controller-manager

Node:
  - kubelet
  - kube-proxy
  - container runtime

Add-ons:
  - CoreDNS
  - Dashboard
  - Metrics Server
```

---
# Kubernetes Object Types Overview

## 1️⃣ Workload Objects
Workload objects manage how applications run on Kubernetes, ensuring scalability, reliability, and lifecycle management.

- **Pod**: The smallest deployable unit, containing one or more containers.
- **ReplicaSet**: Ensures a specified number of identical Pods are running.
- **Deployment**: Manages ReplicaSets and allows rolling updates.
- **StatefulSet**: Manages stateful applications with persistent storage.
- **DaemonSet**: Ensures a copy of a Pod runs on every node.
- **Job**: Runs a task once and ensures it completes.
- **CronJob**: Runs Jobs on a scheduled basis (like a cron task).

---

## 2️⃣ Service Objects
Service objects define networking and communication within the cluster, ensuring connectivity between workloads and external traffic routing.

- **Service**: Exposes a set of Pods as a network service.
- **Ingress**: Routes HTTP(S) traffic to Services using domain-based routing.
- **NetworkPolicy**: Controls traffic between Pods.

---

## 3️⃣ Storage Objects
Storage objects handle persistent data storage and configuration management for applications.

- **PersistentVolume (PV)**: Represents actual storage (e.g., NFS, AWS EBS, GCE Persistent Disk).
- **PersistentVolumeClaim (PVC)**: Requests a specific amount of storage from a PV.
- **StorageClass**: Defines dynamic storage provisioning.
- **ConfigMap**: Stores non-sensitive config data (key-value pairs).
- **Secret**: Stores sensitive information securely (e.g., passwords, API keys).

---

## 4️⃣ Configuration, Policy & Security Objects
These objects help manage cluster security, access control, resource allocation, and policy enforcement.

- **Namespace**: Isolates resources within the cluster.
- **ResourceQuota**: Limits CPU, memory, and storage usage in a Namespace.
- **LimitRange**: Defines min/max resource limits per Pod or Container.
- **HorizontalPodAutoscaler (HPA)**: Automatically scales Pods based on CPU/memory usage.
- **VerticalPodAutoscaler (VPA)**: Adjusts CPU/memory limits for Pods automatically.
- **ServiceAccount**: Grants permissions to Pods to access the Kubernetes API.
- **Role & RoleBinding**: Defines fine-grained permissions for a Namespace.
- **ClusterRole & ClusterRoleBinding**: Grants permissions cluster-wide.

---

