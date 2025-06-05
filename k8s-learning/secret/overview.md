# Kubernetes Secret

## Overview
A **Secret** in Kubernetes is an object used to store sensitive information such as passwords, API keys, SSH keys, or TLS certificates. Secrets help keep sensitive data out of Pod specifications and prevent accidental exposure in logs.


### 2. Define a Secret in YAML
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: YWRtaW4=   # Base64 encoded 'admin'
  password: U3VwZXJTZWNyZXQxMjM=  # Base64 encoded 'SuperSecret123'
```
To apply:
```sh
kubectl apply -f secret.yaml
```

### 3. Using Secret in a Pod
A Pod can use a Secret as environment variables:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-demo
spec:
  containers:
    - name: my-container
      image: busybox
      command: [ "sh", "-c", "echo Username: $USERNAME && echo Password: $PASSWORD" ]
      env:
        - name: USERNAME
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: username
        - name: PASSWORD
          valueFrom:
            secretKeyRef:
              name: my-secret
              key: password
```

Apply and check logs:
```sh
kubectl apply -f pod.yaml
kubectl logs secret-demo
```

### 4. Mounting Secret as a Volume
You can also mount Secrets as files inside a Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-volume-demo
spec:
  volumes:
    - name: secret-volume
      secret:
        secretName: my-secret
  containers:
    - name: my-container
      image: busybox
      command: [ "sh", "-c", "cat /etc/secret-volume/username" ]
      volumeMounts:
        - name: secret-volume
          mountPath: "/etc/secret-volume"
          readOnly: true
```

To check the mounted secret:
```sh
kubectl exec secret-volume-demo -- cat /etc/secret-volume/username
```

## Conclusion
Kubernetes Secrets provide a secure way to manage sensitive data. They can be used as:
- Environment variables
- Mounted volumes
- Referenced in other Kubernetes resources

Secrets are **Base64-encoded**, not encrypted by default. For enhanced security, consider **encryption at rest** and **RBAC restrictions**.

---

