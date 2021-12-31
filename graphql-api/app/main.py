from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter

from .api.queries import Query
from .api.mutations import Mutation


app = FastAPI()

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQLRouter(schema, graphiql=True)
app.include_router(graphql_app, prefix="/graphql")
