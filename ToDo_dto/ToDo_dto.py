import graphene

class TaskInputObject(graphene.InputObjectType):
    title=graphene.String()
    description=graphene.String()
    end_date=graphene.DateTime()
    priority=graphene.Int()
  
    
class TaskOutputObject(graphene.ObjectType):
    task_id = graphene.UUID()
    title=graphene.String()
    description=graphene.String()
    end_date=graphene.DateTime()
    priority=graphene.Int()
    status=graphene.String()
    is_active=graphene.Boolean()
    created_at=graphene.DateTime()
    updated_at=graphene.DateTime()
    