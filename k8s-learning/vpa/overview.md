# Vertical Pod Autoscaler (VPA)

## Overview
Vertical Pod Autoscaler (VPA) automatically adjusts the CPU and memory requests/limits for pods based on their usage patterns. This helps optimize resource utilization and prevents over-provisioning or under-provisioning of resources.

### **Key Components**
1. **VPA Recommender**: Monitors resource usage and provides recommendations.
2. **VPA Updater**: Evicts pods when an update is required.
3. **VPA Admission Controller**: Sets resource requests for newly created pods.

### **Modes**
- **Off**: Only generates recommendations, does not apply changes.
- **Initial**: Applies recommendations only when the pod is created.
- **Auto**: Evicts and recreates pods with updated requests/limits.

## Example: Deploying Vertical Pod Autoscaler

### **Step 1: Install VPA**
```sh
kubectl apply -f https://github.com/kubernetes/autoscaler/releases/latest/download/vertical-pod-autoscaler.yaml
```

### **Step 3: Create a VPA Resource**
```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind:       "Deployment"
    name:       "my-app"
  updatePolicy:
    updateMode: "Auto"
```

### **Step 4: Apply the VPA Resource**
```sh
kubectl apply -f vpa.yaml
```

### **Step 5: Monitor VPA Recommendations**
```sh
kubectl get vpa my-app-vpa --output yaml
```

### **Step 6: Observe the Changes**
VPA will automatically update resource requests based on observed usage. If set to `Auto`, it will evict and restart pods with new resource limits.

## Best Practices
- Use `Off` mode initially to observe recommendations before applying changes.
- Combine VPA with Horizontal Pod Autoscaler (HPA) for optimal scaling.
- Ensure workloads tolerate restarts if using `Auto` mode.
- Avoid setting hard CPU/memory limits in deployments to allow flexibility.

## Summary
Vertical Pod Autoscaler helps in dynamically managing resource requests for pods. By analyzing resource usage, it optimizes pod efficiency and minimizes wastage.

