# Cassandra Architecture

## Overview

Apache Cassandra is a highly scalable, distributed NoSQL database designed for handling large amounts of data across multiple nodes with no single point of failure. It follows a decentralized, peer-to-peer architecture to ensure high availability and fault tolerance.

## Key Components

### 1. **Cluster**

A **cluster** is a collection of nodes that work together as a single database system. It can span multiple physical or virtual machines.

### 2. **Datacenter (DC)**

A **datacenter** is a logical group of nodes within a cluster. A cluster can have one or more datacenters. Datacenters help in workload isolation, geographical distribution, and replication strategies.

### 3. **Node**

A **node** is the basic unit of storage in Cassandra. Each node stores a portion of the data and communicates with other nodes using the gossip protocol.

### 4. **Keyspace**

A **keyspace** is similar to a database in relational systems. It defines:

- Replication strategy
- Number of replicas
- Placement of replicas across datacenters

### 5. **Tables**

Tables store data in **rows and columns**, similar to relational databases but optimized for scalability. Tables in Cassandra support flexible schema design.

### 6. **Partition & Replication**

- **Partitioning**: Data is distributed across nodes based on a **partition key**.
- **Replication**: Data is duplicated across multiple nodes for fault tolerance. The **replication factor** determines how many copies of data exist.

### 7. **Consistency Levels**

Cassandra allows tuning consistency based on read/write requirements. Examples:

- **ONE**: Acknowledgement from one replica.
- **QUORUM**: Majority of replicas must acknowledge.
- **ALL**: All replicas must acknowledge.

### 8. **Gossip Protocol**

A peer-to-peer communication protocol that allows nodes to share state information and detect failures.

### 9. **Commit Log & Memtable**

- **Commit Log**: A persistent log for durability before data is written to memory.
- **Memtable**: An in-memory structure that temporarily holds writes before flushing to disk as an **SSTable**.

### 10. **SSTables (Sorted String Tables)**

Immutable, disk-based storage files where data is written after being flushed from Memtable.

### 11. **Compaction**

A process of merging SSTables to optimize read performance and remove deleted data.

## Data Flow in Cassandra

### **Write Operation**

1. Data is written to the **Commit Log**.
2. Data is then stored in **Memtable**.
3. Periodically, Memtable is flushed to **SSTables** on disk.
4. **Compaction** merges SSTables to improve efficiency.

### **Read Operation**

1. Cassandra checks **Memtable** for recent writes.
2. If data is not found, it searches **SSTables**.
3. **Bloom Filters** help in locating SSTables quickly.
4. Data is merged and returned to the client.

## Conclusion

Cassandra's decentralized, fault-tolerant, and highly available design makes it an excellent choice for big data applications requiring horizontal scalability. Understanding its architecture helps in optimizing performance and ensuring efficient data distribution across clusters.
