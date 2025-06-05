# ReplicaSet Overview

## What is a ReplicaSet?
A **ReplicaSet** is a Kubernetes resource that ensures a specified number of identical **Pods** are running at all times. If a Pod crashes or is deleted, the ReplicaSet automatically creates a new Pod to replace it. It is often used as part of a **Deployment**.

## Key Features:
- **Ensures a desired number of Pod replicas** are running.
- **Automatically replaces failed Pods**.
- **Uses label selectors** to manage Pods.
- **Not usually managed directly**—Deployments are preferred for rolling updates.

## Key Takeaways
- A **ReplicaSet ensures high availability** by maintaining a set number of Pods.
- It **does not handle rolling updates**—use **Deployments** instead for that.
- It **uses label selectors** to manage Pods.
- The **`spec.template` defines the Pod**, similar to a standalone Pod definition.


