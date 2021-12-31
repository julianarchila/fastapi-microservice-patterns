import strawberry
from typing import List

from .types import PersonType, FilmType
from ..db.fake_db import database


@strawberry.type(description="Read operations of the API.")
class Query:

    @strawberry.field(description="Read all persons.")
    async def persons(self) -> List[PersonType]:
        persons: List[PersonType] = []
        for p in database["Persons"]:
            person = PersonType.from_pydantic(p)
            persons.append(person)
        return persons

    @strawberry.field(description="Read all films.")
    async def films(self) -> List[FilmType]:
        films: List[FilmType] = []
        for f in database["Films"]:
            film = FilmType.from_pydantic(f)
            films.append(film)
        return films
