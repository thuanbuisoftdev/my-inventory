# Horizontal Pod Autoscaler (HPA) in Kubernetes

## Overview
Horizontal Pod Autoscaler (HPA) automatically scales the number of pods in a deployment, replication controller, or stateful set based on CPU or memory utilization.

### Key Features:
- Adjusts the number of pods dynamically based on observed metrics.
- Uses CPU utilization by default but can be configured for custom or external metrics.
- Ensures efficient resource utilization and high availability.

## How HPA Works
1. **Monitors Metrics**: HPA collects resource usage from Metrics Server.
2. **Calculates Desired Replicas**: Uses a target metric (e.g., 50% CPU utilization) to determine the necessary number of pods.
3. **Scales Up/Down**: Adjusts the number of pods accordingly.
4. **Ensures Stability**: Avoids rapid scaling by implementing stabilization windows and thresholds.

## Example: Deploying HPA

### Step 1: Install Metrics Server
Ensure that the Kubernetes Metrics Server is running:
```sh
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl edit deployment metrics-server -n kube-system
- --kubelet-insecure-tls
```

## Summary
- HPA automatically scales pods based on resource usage.
- Requires Metrics Server to gather pod metrics.
- Can be customized for different metrics beyond CPU and memory.

This example provides a simple HPA setup for CPU-based autoscaling. You can extend it to include custom or external metrics as needed.

