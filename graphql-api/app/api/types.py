import strawberry
from ..models.person import Person
from ..models.film import Film


@strawberry.experimental.pydantic.type(model=Person, all_fields=True, description="A single person.")
class PersonType:
    pass


@strawberry.experimental.pydantic.type(model=Film, all_fields=True, description="A single film.")
class FilmType:
    pass


@strawberry.experimental.pydantic.input(model=Person, description="Input for creating a single person.")
class PersonCreateInput:
    name: strawberry.auto
    height: strawberry.auto
    mass: strawberry.auto
