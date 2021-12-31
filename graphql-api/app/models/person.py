from pydantic import BaseModel, Field, validator
from pydantic.types import UUID1
from uuid import uuid1


class HeightError(ValueError):
    pass


class Person(BaseModel):
    id: UUID1 = Field(default_factory=uuid1)
    name: str
    height: int
    mass: float

    @validator('height')
    def height_must_be_within_boundaries(cls, v):
        lower_bound: int = 10
        upper_bound: int = 1000
        if v < lower_bound:
            raise HeightError('person is too small')
        elif v > upper_bound:
            raise HeightError('person is too big')
        return v
