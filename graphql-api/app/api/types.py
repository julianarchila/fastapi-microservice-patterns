import strawberry
from ..models import Person, Film


@strawberry.experimental.pydantic.type(model=Person, all_fields=True)
class PersonType:
    pass


@strawberry.experimental.pydantic.type(model=Film, all_fields=True)
class FilmType:
    pass


@strawberry.experimental.pydantic.input(model=Person)
class PersonCreateInput:
    name: strawberry.auto
    height: strawberry.auto
    mass: strawberry.auto


#@strawberry.experimental.pydantic.input(model=Person)
#class PersonUpdateInput:
#    name: Optional[str]
#    height: Optional[int]
#    mass: Optional[float]
