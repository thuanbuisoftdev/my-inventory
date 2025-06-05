from .cassandra import setup_cassandra, CassandraConfig
from . import user_repository

setup_cassandra(CassandraConfig(
    contact_points=["cassandra"],
    port=9042,
    keyspace="learn",
))

print("keyspaces")
print(user_repository.get_users())

