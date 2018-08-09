import graphene
from flask_graphql import GraphQLView

from app.schema.fields import ResponseMessageField
from app.schema.mutations import Mutation
from app.schema.queries import Query


class Schema:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        schema = graphene.Schema(query=Query, mutation=Mutation)

        app.add_url_rule(
            '/graphql',
            view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=app.config['GRAPHIQL'])
        )
        print('[INFO] GraphQLView was successfully added with GraphiQL:{0}'.format(app.config['GRAPHIQL']))
