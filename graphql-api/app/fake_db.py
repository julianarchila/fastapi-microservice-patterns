from typing import Dict, Union, List

from .models import Person, Film


_seed = {
    "Persons": [
        {"name": "Luke Skywalker", "height": 172, "mass": 77.0},
	    {"name": "C-3PO", "height": 167, "mass": 75.0},
    ],
    "Films": [
        {"episode_id": 1, "title": "The Phantom Menace"},
        {"episode_id": 2, "title": "Attack of the Clones"}
    ]
}


def fake_database_factory() -> Dict:
    database: Dict[str, List[Union[Person, Film]]] = {"Persons": [], "Films": []}
    database["Persons"].append(Person(**_seed["Persons"][0]))
    database["Persons"].append(Person(**_seed["Persons"][1]))
    database["Films"].append(Film(episode_id=_seed["Films"][0]["episode_id"], title=_seed["Films"][0]["title"], characters=[Person(**_seed["Persons"][0])]))
    database["Films"].append(Film(episode_id=_seed["Films"][1]["episode_id"], title=_seed["Films"][1]["title"], characters=[Person(**_seed["Persons"][0]), Person(**_seed["Persons"][0])]))
    return database

database = fake_database_factory()
