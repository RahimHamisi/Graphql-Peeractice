import graphene

from ToDo_builder.ToDo_builder import TodoBuilder
from ToDo_dto.ToDo_dto import TaskOutputObject

class TaskQuery(graphene.ObjectType):
    all_task=graphene.List(TaskOutputObject)
    detailed_task=graphene.Field(TaskOutputObject,task_id=graphene.UUID(required=True))
    
    def resolve_all_task():
        return TodoBuilder.get_all_task()
    
    def resolve_detailde_task(task_id):
        return TodoBuilder.get_task(task_id=task_id)
    