# Kubernetes DaemonSet Overview

## What is a DaemonSet?
A **DaemonSet** ensures that a specific Pod runs **on all (or some) nodes** in a Kubernetes cluster.

## Use Cases
✅ Running cluster-wide services on every node:
- **Log collectors** (e.g., Fluentd, Logstash)
- **Monitoring agents** (e.g., Prometheus Node Exporter)
- **Security agents** (e.g., Falco, antivirus scanners)
- **Storage daemons** (e.g., Ceph, GlusterFS)

## Key Features
- Automatically **adds a Pod to every new node** in the cluster.
- Can run Pods **only on specific nodes** using **node selectors or taints & tolerations**.
- **Deletes Pods automatically** if a node is removed.

---

## Pros & Cons of DaemonSet

| Feature             | DaemonSet |
|--------------------|-----------|
| Ensures a Pod runs on all nodes | ✅ Yes |
| Auto-deploys on new nodes | ✅ Yes |
| Good for logging/monitoring | ✅ Yes |
| Load balancing | ❌ No |
| Scales based on demand | ❌ No (Fixed: 1 Pod per node) |

---
