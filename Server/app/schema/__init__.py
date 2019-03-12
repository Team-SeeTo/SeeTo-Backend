import json
import graphene
from flask_graphql import GraphQLView
from flask import redirect

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
        
        schema_json = schema.introspect()
        
        @app.route('/schema')
        def schemajson():
            return json.dump(schema_json)

        @app.route('/')
        def to_graphql():
            return redirect('/graphql')

        print('[INFO] GraphQLView was successfully added with GraphiQL:{0}'.format(app.config['GRAPHIQL']))
