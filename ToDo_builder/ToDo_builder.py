from ToDo_app.models import *
from ToDo_dto.ToDo_dto import TaskOutputObject


class TodoBuilder:
    def get_all_task():
        tasks=Task.objects.filter(is_active=True)
        all_tasks=[]
        for task in tasks:
            result=TaskOutputObject(
                task_id=task.task_id,
                title=task.title,
                description=task.description,
                status=task.status,
                is_active=task.is_active,
                created_at=task.created_at,
                updated_at=task.updated_at
                
            )
            all_tasks.append(result)
        return all_tasks
    
    def get_task(task_id):
        try:
            task=Task.objects.get(task_id=task_id)
            single_task=[]
            
            task_data=TaskOutputObject(
                     task_id=task.task_id,
                title=task.title,
                description=task.description,
                status=task.status,
                is_active=task.is_active,
                created_at=task.created_at,
                updated_at=task.updated_at
                
            )
            single_task.append(task_data)
        except Task.DoesNotExist:
            return  f"No Task availabe with that id"
        
        return single_task