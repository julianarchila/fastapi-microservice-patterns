import strawberry

from .types import PersonCreateInput, PersonType
from ..models import Person
from ..fake_db import database


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_person(self, person: PersonCreateInput) -> PersonType:
        person_pydantic = Person(name=person.name, height=person.height, mass=person.mass)
        database["Persons"].append(person_pydantic)
        return PersonType.from_pydantic(person_pydantic)
