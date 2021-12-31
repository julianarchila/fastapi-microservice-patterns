import strawberry
from typing import List

from .types import PersonType, FilmType
from ..fake_db import database


@strawberry.type
class Query:

    @strawberry.field
    def persons(self) -> List[PersonType]:
        persons: List[PersonType] = []
        for p in database["Persons"]:
            person = PersonType.from_pydantic(p)
            persons.append(person)
        return persons

    @strawberry.field
    def films(self) -> List[FilmType]:
        films: List[FilmType] = []
        for f in database["Films"]:
            film = FilmType.from_pydantic(f)
            films.append(film)
        return films
