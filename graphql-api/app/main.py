from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .api.schema import schema


app = FastAPI()

graphql_app = GraphQLRouter(schema, graphiql=True)
app.include_router(graphql_app, prefix="/graphql")
