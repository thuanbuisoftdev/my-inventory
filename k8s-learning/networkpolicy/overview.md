# Kubernetes NetworkPolicy Overview

## 📌 What is a NetworkPolicy?
A **NetworkPolicy** in Kubernetes is a resource that controls network traffic **between pods** and **from external sources** based on defined rules. It acts as a firewall at the pod level, improving **security and isolation** within a cluster.

### 🔹 Key Features:
- Restricts **incoming** (`ingress`) and/or **outgoing** (`egress`) traffic.
- Works **only with network plugins** that support it (e.g., Calico, Cilium, WeaveNet).
- Applies **at the pod level**, not at the node or service level.

🔹 **Explanation:**
- The **webserver** pod is accessible from **any external IP**.
- Useful for exposing public-facing services.

## 🚀 Summary
| Feature          | Description |
|-----------------|-------------|
| **Security**    | Controls network traffic at the pod level. |
| **Pod Isolation** | Blocks unwanted access to sensitive pods. |
| **Custom Rules** | Allows fine-grained network access control. |
| **Plugin Support** | Requires a compatible CNI (e.g., Calico, Cilium). |

NetworkPolicies help **secure Kubernetes workloads** by defining clear networking rules. 🚀

