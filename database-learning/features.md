# Database Core Features

## 1. **Data Model**

- **Relational (SQL)**: Structured, table-based storage (e.g., MySQL, PostgreSQL).
- **NoSQL**: Flexible schemas for different data types:
  - **Key-Value Stores** (e.g., Redis, DynamoDB)
  - **Document Stores** (e.g., MongoDB, CouchDB)
  - **Column-Family Stores** (e.g., Cassandra,
  HBase)
  - **Graph Databases** (e.g., Neo4j, ArangoDB)

## 2. **Query Language & APIs**

- **SQL**: Declarative language for structured queries.
- **NoSQL Query Languages**: JSON-based (MongoDB), Graph Traversal (Cypher for Neo4j).
- **ORMs & Query Builders**: SQLAlchemy, Hibernate, Prisma.

## 3. **Indexing**

- Improves query performance by creating efficient lookup structures.
- Types:
  - **Primary Index**: Based on primary key.
  - **Secondary Index**: For fast lookups on non-primary attributes.
  - **B-Tree, Hash Index, Bitmap Index**: Various indexing techniques.

## 4. **Transactions & Concurrency Control**

- **ACID Properties** (Atomicity, Consistency, Isolation, Durability) ensure reliable operations.
- **Isolation Levels**:
  - Read Uncommitted, Read Committed, Repeatable Read, Serializable.
- **Concurrency Mechanisms**:
  - Locking (Pessimistic, Optimistic), Multi-Version Concurrency Control (MVCC).

## 5. **Scalability, Sharding & Replication**

- **Sharding**: Splits large databases into smaller partitions for scalability.
- **Replication**: Duplicates data for redundancy and performance.
  - **Master-Slave Replication**: Read from replicas, write to master.
  - **Multi-Master Replication**: Multiple writable nodes.
- **Vertical Scaling**: Adding more resources (CPU, RAM) to a single node.
- **Horizontal Scaling**: Distributing load across multiple nodes.
- **Load Balancing**: Evenly distributes traffic to avoid bottlenecks.

## 6. **Security & Access Control**

- **Authentication & Authorization**: Role-Based Access Control (RBAC), LDAP, OAuth.
- **Encryption**:
  - At Rest (AES, TDE), In Transit (TLS/SSL).
- **Auditing & Logging**: Tracks data access and modifications.

## 7. **Backup & Recovery**

- **Snapshot Backups**: Periodic full backups.
- **Incremental Backups**: Store changes since the last backup.
- **Point-in-Time Recovery (PITR)**: Restore database state at a specific time.

## **Conclusion**

Databases continue evolving with new technologies for performance, scalability, and flexibility. Choosing the right database depends on specific use cases and requirements.
