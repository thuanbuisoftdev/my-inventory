# Replication Controller in Kubernetes

## Overview
ReplicationController ensures that a specified number of pod replicas are running at all times in a Kubernetes cluster. If a pod fails, it automatically creates a new one to maintain the desired state.

### **Key Features**:
- Ensures a specific number of pod replicas are always running.
- Automatically replaces failed pods.
- Supports rolling updates and scaling.
- Works similarly to Deployments but is now **deprecated** in favor of ReplicaSets.

## **ReplicationController vs ReplicaSet**
| Feature | ReplicationController | ReplicaSet |
|---------|---------------------|------------|
| Supports Set-Based Selectors | ❌ No | ✅ Yes |
| Used in Deployments | ❌ No | ✅ Yes |
| Recommended for New Deployments | ❌ No | ✅ Yes |

**Note:** ReplicationControllers are **deprecated** in favor of ReplicaSets & Deployments.

## **Conclusion**
While **ReplicationController** was historically used to manage pod replication, it has been replaced by **ReplicaSet and Deployment**, which provide more advanced features like rolling updates. However, you may still encounter ReplicationController in older Kubernetes configurations.

