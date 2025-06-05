# Kubernetes Pods Overview

## **What is a Pod?**
A **Pod** is the smallest deployable unit in Kubernetes. It represents a single instance of a running application. A Pod can contain **one or more containers** that share the same storage and network namespace.

### **Key Features of Pods:**
- **Single-container Pods:** The most common use case where a Pod runs a single application.
- **Multi-container Pods:** Containers in the same Pod share storage and networking. Useful for tightly coupled services (e.g., sidecar patterns).
- **Short-lived or long-running:** Pods are ephemeral, meaning they can be created and destroyed dynamically by higher-level controllers like Deployments or Jobs.

## **When to Use a Pod Directly?**
✅ Testing a simple application.
✅ Running a one-off job.
✅ Debugging a containerized app.
❌ **For production workloads, use Deployments or StatefulSets instead.**


