# LimitRange in Kubernetes

## Overview

A **LimitRange** in Kubernetes is a policy that sets default resource requests and limits for containers within a namespace. It helps enforce constraints on CPU, memory, and other resources at the **Pod or Container level** to prevent resource exhaustion by a single workload.

- **Ensures fair resource distribution** within a namespace.
- **Prevents excessive resource allocation** by setting maximum limits.
- **Sets default resource requests and limits** when not explicitly defined in a Pod.

A LimitRange is applied per **namespace** and affects all workloads within that namespace.

---

## Example: LimitRange YAML Definition

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: example-limitrange
  namespace: my-namespace
spec:
  limits:
  - type: Container
    max:
      cpu: "2"
      memory: "2Gi"
    min:
      cpu: "100m"
      memory: "256Mi"
    default:
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:
      cpu: "250m"
      memory: "256Mi"
```

---

## Explanation
- **max:** The maximum CPU/memory a container can request (2 CPU cores, 2Gi memory).
- **min:** The minimum CPU/memory a container must request (100m CPU, 256Mi memory).
- **default:** The default CPU/memory limits applied to a container if not explicitly defined.
- **defaultRequest:** The default resource request assigned if not set in the Pod spec.

---

## Applying the LimitRange
To apply the LimitRange to your cluster, use:
```sh
kubectl apply -f limitrange.yaml
```

To check applied LimitRanges in a namespace:
```sh
kubectl get limitrange -n my-namespace
```

To describe a specific LimitRange:
```sh
kubectl describe limitrange example-limitrange -n my-namespace
```

---

## Summary
- **LimitRange applies at the Container level** within a namespace.
- **ResourceQuota applies at the Namespace level** to control overall resource consumption.
- Both work together to **ensure efficient resource allocation** in Kubernetes clusters.

