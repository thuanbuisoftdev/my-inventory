from pydantic import BaseModel
from .cassandra import connect_db


class User(BaseModel):
    user_id: int
    name: str
    age: int


def list_users() -> list[User]:
    users = []
    with connect_db() as db:
        users = [
            User(
                user_id=row.user_id,
                name=row.name,
                age=row.age,
            )
            for row in db.execute("SELECT * FROM user;")
        ]

    return users
