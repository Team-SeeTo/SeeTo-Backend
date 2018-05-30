import graphene
from functools import wraps
from flask_jwt_extended import get_jwt_identity, get_raw_jwt, jwt_required, jwt_refresh_token_required
from flask_graphql import GraphQLView
from app.GraphQL.mutations import Mutation
from app.GraphQL.queries import Query


class Schema:
    def __init__(self, app):
        schema = graphene.Schema(query=Query, mutation=Mutation)

        app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=app.config['GRAPHIQL'])
        )
        print('[INFO] GraphQLView was successfully added with GraphiQL:{0}'.format(app.config['GRAPHIQL']))
