from typing import List

from app.db import convert_inbound_factory, convert_outbound_factory
from app.models.knowledge_base_models import DBKbResource
from app.schema.kb_resource_schema import KBResourceIn

convert_inbound = convert_inbound_factory("kb_resource_id")
convert_outbound = convert_outbound_factory("kb_resource_id")

async def get_kb_resource_by_id(kb_resource_id: str) -> DBKbResource:
    db_kb_resource = DBKbResource.objects(id=kb_resource_id).first()
    return convert_inbound(db_kb_resource)

async def get_kb_resources_by_knowledge_base(knowledge_base_id: str) -> List[DBKbResource]:
    db_kb_resources = DBKbResource.objects(knowledgeBase=knowledge_base_id)
    return [convert_inbound(kb_resource) for kb_resource in db_kb_resources]

async def get_kb_resources_by_owner(owner_id: str) -> List[DBKbResource]:
    db_kb_resources = DBKbResource.objects(ownerId=owner_id)
    return [convert_inbound(db_kb_resource) for db_kb_resource in db_kb_resources]

async def save_kb_resource(kb_resource: KBResourceIn) -> DBKbResource:
    db_kb_resource = DBKbResource(**convert_outbound(kb_resource))
    db_kb_resource.save()
    return convert_inbound(db_kb_resource)

async def update_kb_resource(kb_resource: KBResourceIn) -> DBKbResource:
    db_kb_resource = DBKbResource.objects(id=kb_resource.kb_resource_id).first()
    db_kb_resource.update(**convert_outbound(kb_resource))
    return convert_inbound(db_kb_resource)

async def delete_kb_resource(kb_resource_id: str) -> DBKbResource:
    db_kb_resource = DBKbResource.objects(id=kb_resource_id).first()
    db_kb_resource.delete()
    return convert_inbound(db_kb_resource)