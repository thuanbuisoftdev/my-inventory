# Horizontal Pod Autoscaler (HPA) vs. Vertical Pod Autoscaler (VPA)

## Horizontal Pod Autoscaler (HPA)
HPA automatically scales the number of pod replicas based on observed CPU, memory, or custom metrics.

### Key Features:
- Adjusts the number of pods dynamically.
- Uses CPU/Memory utilization or external metrics.
- Works well for stateless applications.
- Requires Metrics Server to function.

## Vertical Pod Autoscaler (VPA)
VPA automatically adjusts resource requests and limits for individual containers.

### Key Features:
- Modifies CPU/Memory requests and limits.
- Reduces underutilization and over-provisioning.
- Works well for stateful applications.
- Can function in "off", "auto", or "recreate" modes.

## Comparison Table
| Feature                | HPA                          | VPA                          |
|------------------------|-----------------------------|-----------------------------|
| Scaling Type          | Number of pod replicas     | Resource requests/limits   |
| Suitable for          | Stateless applications     | Stateful applications      |
| Metrics Used         | CPU, Memory, External     | CPU, Memory               |
| Update Strategy      | Creates/destroys pods      | Adjusts container resources |
| Requires Restart     | No                          | Yes (in certain modes)      |
| Works with HPA       | Yes                         | Yes                         |

## Conclusion
- **Use HPA** when scaling out workloads horizontally for stateless applications.
- **Use VPA** when adjusting resource requests dynamically to optimize pod efficiency.
- **Use both together** to get the best of horizontal and vertical scaling.

