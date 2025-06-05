# PersistentVolume (PV) in Kubernetes

## Overview

A **PersistentVolume (PV)** in Kubernetes is a storage resource that provides a way to manage persistent data independently from pods and their lifecycle. PVs abstract storage implementation details and allow dynamic provisioning of storage.

### Key Features:
- **Decouples storage from pods**: Storage exists independently of pod lifecycle.
- **Supports multiple storage backends**: Local disks, NFS, cloud storage (AWS EBS, GCE PD, etc.).
- **Managed by administrators**: Users request storage via PersistentVolumeClaims (PVCs).

## PersistentVolume Lifecycle

1. **Provisioning**: PVs are created manually by administrators or dynamically via StorageClasses.
2. **Binding**: Users create PersistentVolumeClaims (PVCs) that request specific storage properties.
3. **Using**: Pods mount the claimed PV to access persistent storage.
4. **Reclaiming**: When a PVC is deleted, the PV enters a reclaim phase (Retain, Delete, or Recycle).

### 3. Use the PVC in a Pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  volumes:
    - name: storage-volume
      persistentVolumeClaim:
        claimName: example-pvc
  containers:
    - name: app-container
      image: nginx
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: storage-volume
```

## Reclaim Policies
- **Retain**: PV is not deleted; data remains for manual recovery.
- **Recycle**: Simple scrub and reuse (deprecated).
- **Delete**: PV is removed permanently when PVC is deleted.

## Summary
- PVs provide persistent storage abstraction in Kubernetes.
- PVCs allow users to request storage resources.
- Pods use PVCs to mount storage and persist data beyond pod lifecycle.

This ensures efficient and scalable storage management in Kubernetes! 🚀

