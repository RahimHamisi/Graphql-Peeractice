import graphene
from ToDo_app.schema import TaskQuery
from ToDo_app.views import TaskMutation


class Query(TaskQuery):
    pass


class Mutation(TaskMutation,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)