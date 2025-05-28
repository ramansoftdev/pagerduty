import abc
from enum import Enum
from typing import TypedDict


class Role(Enum):
    ENGINEER = "engineer"
    MANAGER = "manager"


class User(TypedDict):
    id: int
    name: str
    role: Role


class AuthServiceAbstract(abc.ABC):
    @abc.abstractmethod
    def get_user(self, id: int) -> User | None:
        pass