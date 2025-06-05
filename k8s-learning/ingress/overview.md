# Kubernetes Ingress

## Overview
Kubernetes **Ingress** is an API object that manages external access to services within a cluster. It provides HTTP(S) routing, domain-based traffic management, and SSL termination without exposing services via `NodePort` or `LoadBalancer`.

## Features
- **Path-based routing**: Route requests based on URL paths.
- **Host-based routing**: Route traffic based on domains.
- **SSL/TLS termination**: Manage HTTPS traffic with certificates.
- **Load balancing**: Distribute traffic across multiple backend services.

## Prerequisites
- A Kubernetes cluster with an **Ingress Controller** (e.g., Nginx Ingress Controller, Traefik, or AWS ALB Ingress Controller).
- A `Service` that the Ingress will route traffic to.

## Installation

To set up an Ingress Controller, you can use one of the following methods:

### Using Minikube
Enable the Ingress addon in Minikube:
```bash
minikube addons enable ingress
```

### Using Helm
Add the NGINX Ingress Controller Helm repository:
```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
```

Install the NGINX Ingress Controller:
```bash
helm install ingress-nginx ingress-nginx/ingress-nginx \
    --namespace ingress-nginx \
    --create-namespace
```