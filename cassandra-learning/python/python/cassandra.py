from cassandra.cluster import Cluster, ResultSet, Session
from pydantic import BaseModel
from contextlib import contextmanager
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.FileHandler("cassandra.log"))


class CassandraConfig(BaseModel):
    contact_points: list[str] = ["127.0.01"]
    port: int = 9042
    keyspace: str = ""


class CassandraDb:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, statement: str) -> ResultSet:
        return self.session.execute(statement)


class CassandraClient:
    def __init__(self, config: CassandraConfig):
        self.config = config
        self.cluster = Cluster(contact_points=config.contact_points, port=config.port)

    @contextmanager
    def connect_db(self, keyspace: str = None):
        session = self.cluster.connect(keyspace or self.config.keyspace)
        LOGGER.debug(f"session connected: {session.session_id}")
        try:
            yield CassandraDb(session)
        except Exception as e:
            print(e)
        finally:
            LOGGER.debug(f"session shutdown: {session.session_id}")
            session.shutdown()


DEFAULT_CASSANDRA_CONFIG = CassandraConfig()
_CASSANDRA_DB = None


def setup_cassandra(config: CassandraConfig = None) -> None:
    global _CASSANDRA_DB
    if not _CASSANDRA_DB:
        _CASSANDRA_DB = CassandraClient(config or DEFAULT_CASSANDRA_CONFIG)


def get_client() -> CassandraClient:
    if not _CASSANDRA_DB:
        raise Exception("Not initialized")
    return _CASSANDRA_DB


def connect_db(keyspace: str = None) -> CassandraDb:
    return get_client().connect_db(keyspace)
