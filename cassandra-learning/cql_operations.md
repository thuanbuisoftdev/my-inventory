# Summary of CQL Syntax Operations

## 1. Keyspace Operations

### Create a Keyspace

```sql
CREATE KEYSPACE my_keyspace
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
```

### Use a Keyspace

```sql
USE my_keyspace;
```

### Alter a Keyspace

```sql
ALTER KEYSPACE my_keyspace
WITH replication = {'class': 'NetworkTopologyStrategy', 'datacenter1': 3, 'datacenter2': 2};
```

### Drop a Keyspace

```sql
DROP KEYSPACE my_keyspace;
```

---

## 2. Table Operations

### Create a Table

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    name text,
    age int,
    email text
);
```

### Alter a Table

```sql
ALTER TABLE users ADD phone text;
```

### Drop a Table

```sql
DROP TABLE users;
```

### Truncate a Table

```sql
TRUNCATE TABLE users;
```

---

## 3. Insert, Update, Delete Operations

### Insert Data

```sql
INSERT INTO users (id, name, age, email)
VALUES (uuid(), 'Alice', 30, 'alice@example.com');
```

### Update Data

```sql
UPDATE users SET age = 31 WHERE id = 123e4567-e89b-12d3-a456-426614174000;
```

### Delete Data

```sql
DELETE FROM users WHERE id = 123e4567-e89b-12d3-a456-426614174000;
```

---

## 4. Query Data

### Select Data

```sql
SELECT * FROM users;
```

### Select Specific Columns

```sql
SELECT name, age FROM users WHERE id = 123e4567-e89b-12d3-a456-426614174000;
```

### Filtering Data

```sql
SELECT * FROM users WHERE age > 25;
```

---

## 5. Index Operations

### Create an Index

```sql
CREATE INDEX ON users(email);
```

### Drop an Index

```sql
DROP INDEX users_email_idx;
```

---

## 6. User and Role Management

### Create a User

```sql
CREATE USER alice WITH PASSWORD 'securepassword' NOSUPERUSER;
```

### Grant Permissions

```sql
GRANT SELECT ON users TO alice;
```

### Revoke Permissions

```sql
REVOKE SELECT ON users FROM alice;
```

### Drop a User

```sql
DROP USER alice;
```

---

## 7. Batch Operations

### Batch Insert and Update

```sql
BEGIN BATCH
    INSERT INTO users (id, name, age, email) VALUES (uuid(), 'Bob', 28, 'bob@example.com');
    UPDATE users SET age = 29 WHERE id = 123e4567-e89b-12d3-a456-426614174000;
APPLY BATCH;
```

This document provides a structured summary of key CQL operations with examples. Let me know if you need further details or modifications!
