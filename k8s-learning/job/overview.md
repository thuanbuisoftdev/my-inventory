# Kubernetes Job Overview

## What is a Job?
A **Job** in Kubernetes ensures that a set of **Pods run to completion**. Unlike Deployments or DaemonSets, Jobs are used for **short-lived, batch processing tasks**.

## Use Cases
✅ Running one-time scripts (e.g., database migrations)  
✅ Batch data processing (e.g., ETL jobs)  
✅ Automated tasks like backups, report generation  
✅ Machine learning model training

## Key Features
- **Ensures successful execution**: Runs a Pod until it completes successfully.
- **Retries on failure**: Can automatically retry failed Pods.
- **Supports parallel execution**: Can run multiple Pods in parallel to complete work faster.
- **Pods are deleted after completion** (configurable via TTL).

---

## Pros & Cons of Job

| Feature             | Job |
|--------------------|-----------|
| Runs once and exits | ✅ Yes |
| Ensures completion | ✅ Yes |
| Supports retries | ✅ Yes |
| Supports parallel execution | ✅ Yes |
| Long-running service | ❌ No (Use Deployments instead) |
| Auto-restarts on node failure | ❌ No (Use CronJobs for periodic tasks) |

---

## When to Use a Job?
✅ When you need a **one-time** execution that must **finish successfully**.  
✅ When you need **batch processing with retries**.  
❌ **Not for long-running services** (use Deployments instead).  
❌ **Not for recurring jobs** (use CronJobs instead).

