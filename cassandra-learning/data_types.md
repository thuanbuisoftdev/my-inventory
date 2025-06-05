# Supported Data Types in Cassandra

Cassandra provides a variety of built-in data types that can be used to define table schemas. These data types are categorized as follows:

## 1. Basic Data Types

- **ascii** – US-ASCII character string
- **bigint** – 64-bit signed integer
- **blob** – Arbitrary bytes (binary data)
- **boolean** – True or false
- **counter** – Distributed counter (64-bit signed integer)
- **decimal** – Variable precision decimal
- **double** – 64-bit IEEE 754 floating point
- **float** – 32-bit IEEE 754 floating point
- **inet** – IP address (IPv4 or IPv6)
- **int** – 32-bit signed integer
- **smallint** – 16-bit signed integer
- **text** – UTF-8 encoded string
- **time** – Time of day without a date
- **timestamp** – Date and time with millisecond precision
- **tinyint** – 8-bit signed integer
- **uuid** – Universally unique identifier (UUID)
- **varchar** – UTF-8 encoded string (alias for text)
- **varint** – Arbitrary-precision integer

## 2. Collection Data Types

Cassandra supports collection data types that allow storing multiple values in a single column:

- **list<type>** – Ordered collection of elements (e.g., list<int>)
- **set<type>** – Unordered collection of unique elements (e.g., set<text>)
- **map<key, value>** – Key-value pairs where both key and value have specified types (e.g., map<text, int>)

## 3. User-Defined Types (UDTs)

Cassandra allows defining custom data types using:

```sql
CREATE TYPE address (
    street text,
    city text,
    zip int
);
```

These UDTs can then be used as column types within tables.

## 4. Tuple Type

Tuples allow grouping multiple fields with different data types in a single column:

```sql
tuples<type1, type2, ...>
```

Example:

```sql
tuples<int, text, boolean>
```

## 5. Special Data Types

- **frozen** – Freezes a collection or UDT, treating it as a single value to prevent modification of its individual elements.
- **duration** – Represents a time duration (days, hours, minutes, etc.).

These data types allow Cassandra to efficiently store and retrieve structured data while supporting a flexible schema.
