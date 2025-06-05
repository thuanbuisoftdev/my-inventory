
# Normalization

A database design process to eliminate duplicates, maintain data integrity

1NF:

- Atomicity: colum contains indivisible value

2NF:

- 1NF
- No partial dependency: non-key columns should depend on primary key, not just a part of it

3NF:

- 2NF
- No transitive dependency: non-key columns should depend only on primary key

# Denormalization

Constrast with normolization to improve read speed
