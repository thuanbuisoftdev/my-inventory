# Kubernetes ServiceAccount Overview

## What is a ServiceAccount?
A **ServiceAccount** in Kubernetes is an identity used by pods to interact with the Kubernetes API securely. Unlike user accounts, which are intended for humans, ServiceAccounts are meant for workloads running inside the cluster.

## Key Features
- Each pod can be associated with a ServiceAccount.
- Default ServiceAccount is automatically assigned if none is specified.
- ServiceAccounts enable fine-grained access control via RBAC (Role-Based Access Control).
- Associated with secrets for authentication.

## When to Use a ServiceAccount?
- When an application running inside a pod needs to interact with the Kubernetes API.
- To restrict access permissions for security hardening.
- To enable workloads to authenticate against external services.


## 3. Assign the ServiceAccount to a Pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: default
spec:
  serviceAccountName: my-service-account
  containers:
  - name: my-container
    image: busybox
    command: ["sleep", "3600"]
```
Apply it using:
```sh
kubectl apply -f pod.yaml
```

# Verifying the ServiceAccount
- Check available ServiceAccounts:
  ```sh
  kubectl get serviceaccounts
  ```
- Describe the ServiceAccount:
  ```sh
  kubectl describe serviceaccount my-service-account
  ```
- Verify Pod’s assigned ServiceAccount:
  ```sh
  kubectl get pod my-pod -o yaml | grep serviceAccountName
  ```

# Conclusion
A **ServiceAccount** in Kubernetes enhances security and access control for workloads interacting with the Kubernetes API. Combining it with RBAC ensures minimal privilege access, improving cluster security.

