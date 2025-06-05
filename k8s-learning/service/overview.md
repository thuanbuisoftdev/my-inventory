# Kubernetes Service Overview

## What is a Kubernetes Service?
A **Service** in Kubernetes is an abstraction that defines a logical set of Pods and enables external or internal access to them. Since Pods are ephemeral (they can be restarted, rescheduled, or deleted), a Service provides a **stable endpoint** to access them.

## Key Features
- **Stable IP & DNS**: Services provide a consistent IP and DNS name for accessing Pods.
- **Load Balancing**: Distributes traffic among multiple Pods.
- **Service Discovery**: Enables other services or clients to find and connect to Pods.
- **Multiple Types**: Supports different networking use cases.

## Service Types
| Type              | Description |
|------------------|-------------|
| `ClusterIP` (default) | Exposes the service internally within the cluster. |
| `NodePort` | Exposes the service on a static port on each node. |
| `LoadBalancer` | Provisions an external load balancer (cloud provider dependent). |
| `ExternalName` | Maps the service to an external DNS name. |

## Example YAML: ClusterIP Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80  # Service port
      targetPort: 8080  # Container port
  type: ClusterIP  # Internal access only
```

## Example YAML: NodePort Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nodeport-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80  # Service port
      targetPort: 8080  # Container port
      nodePort: 30007  # Exposed on each node
  type: NodePort
```

## Example YAML: LoadBalancer Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-loadbalancer-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80  # Service port
      targetPort: 8080  # Container port
  type: LoadBalancer  # Requires cloud provider support
```

## Example YAML: ExternalName Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-service
spec:
  type: ExternalName
  externalName: example.com
```

## Conclusion
Kubernetes Services provide a stable way to access applications running in a cluster. Choosing the right Service type depends on whether the application needs internal or external exposure.

