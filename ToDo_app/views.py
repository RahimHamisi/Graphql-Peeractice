from django.shortcuts import render
import graphene

from .models import Task
from ToDo_dto.ToDo_dto import TaskInputObject, TaskOutputObject

# Create your views here.
class CreateTaskMutation(graphene.Mutation):
    class Arguments:
        input=TaskInputObject()
        
    data=graphene.Field(TaskOutputObject)
    sucess=graphene.Boolean()
    
    @classmethod
    def mutate(cls,root,info,input):
        new_task=Task.object.create(
            title=input.title,
            description=input.description,
            end_date=input.end_date,
            priority=input.priority,
            status=input.status
        )
        new_task.save()
        success=True
        return CreateTaskMutation(data=new_task,sucess=success)
    
    
class UpdateTaskMutation(graphene.Mutation):
    class Arguments:
        input=TaskInputObject()
        task_id = graphene.UUID(required=True)
        
    data=graphene.Field(TaskOutputObject)
    sucess=graphene.Boolean()
    
    @classmethod
    def mutate(cls,root,info,task_id,input):
        try:
            task=Task.object.get(task_id=task_id)
            if task is not  None:
                task.title=input.title,
                task.description=input.description,
                task.end_date=input.end_date,
                task.priority=input.priority,
                task.status=input.status
                success=True
            else:
                success=False
                return None
        except Task.DoesNotExist:
            success=False
            return f"Task with that id is not present"
        return UpdateTaskMutation(data=task,success=success)
        
class DeleteTaskMutation(graphene.Mutation):
    class Arguments:
        task_id = graphene.UUID(required=True)
        
    data=graphene.Field(TaskOutputObject)
    sucess=graphene.Boolean()
    
    @classmethod
    def mutate(cls,root,info,task_id):
        try:
            task=Task.object.get(task_id=task_id)
            task.is_active=False
            task.save()
            success=True
        except:
            return f"Task with that id is not present"
            success=False
        return DeleteTaskMutation(data=task,success=success)

class TaskMutation(graphene.ObjectType):
    create_task=CreateTaskMutation.Field()
    update_task=UpdateTaskMutation.Field()
    delete_task=DeleteTaskMutation.Field()