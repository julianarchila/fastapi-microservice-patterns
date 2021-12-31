from typing import List
from pydantic import BaseModel, Field
from pydantic.types import UUID1
from uuid import uuid1


class Person(BaseModel):
    id: UUID1 = Field(default_factory=uuid1)
    name: str
    height: int
    mass: float


class Film(BaseModel):
    id: UUID1 = Field(default_factory=uuid1)
    episode_id: int
    title: str
    characters: List[Person]
