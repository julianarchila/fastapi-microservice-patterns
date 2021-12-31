# Get all persons

GraphiQL:

```
query {
  persons {
    id
    name
    height
    mass
  }
}
```

# Create a person

GraphiQL:

```
mutation createPerson($person: PersonCreateInput!) {
  createPerson(person: $person) {
    id
    name
    height
    mass
  }
}   
```

Query variables:

```
{
  "person": {
    "name": "R2-D2",
    "height": 96,
    "mass": 32
  }
}
```

# Get all films

... without characters.

GraphiQL:

```
query {
  films {
    id
    title
    episodeId
  }
}
```
