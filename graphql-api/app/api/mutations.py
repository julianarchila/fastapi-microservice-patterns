import strawberry
from typing import Optional

from .types import PersonCreateInput, PersonType
from ..models.person import Person, HeightError
from ..db.fake_db import database


@strawberry.type(description="Create/Update/Delete operations of the API.")
class Mutation:
    @strawberry.mutation(description="Create a single person.")
    async def create_person(self, person: PersonCreateInput) -> Optional[PersonType]:
        try:
            person_pydantic = Person(name=person.name, height=person.height, mass=person.mass)
            database["Persons"].append(person_pydantic)
            return PersonType.from_pydantic(person_pydantic)
        except HeightError:
            return None
