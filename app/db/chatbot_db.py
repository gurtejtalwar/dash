from typing import List

from app.db import convert_inbound_factory, convert_outbound_factory
from app.models.chatbot_models import DBChatbot
from app.schema.chatbot_schema import ChatbotIn

convert_inbound = convert_inbound_factory("chatbot_id")
convert_outbound = convert_outbound_factory("chatbot_id")

async def get_chatbot_by_id(chatbot_id: str) -> DBChatbot:
    db_chatbot = DBChatbot.objects(id=chatbot_id).first()
    return convert_inbound(db_chatbot)

async def get_chatbots_by_owner(owner_id: str) -> List[DBChatbot]:
    db_chatbots = DBChatbot.objects(ownerId=owner_id)
    return [convert_inbound(chatbot) for chatbot in db_chatbots]

async def save_chatbot(chatbot: ChatbotIn) -> DBChatbot:
    db_chatbot = DBChatbot(**convert_outbound(chatbot))
    db_chatbot.save()
    return convert_inbound(db_chatbot)

async def update_chatbot(chatbot: ChatbotIn) -> DBChatbot:
    db_chatbot = DBChatbot.objects(id=chatbot.chatbot_id).first()
    db_chatbot.update(**convert_outbound(chatbot))
    return convert_inbound(db_chatbot)

async def delete_chatbot(chatbot_id: str) -> DBChatbot:
    db_chatbot = DBChatbot.objects(id=chatbot_id).first()
    db_chatbot.delete()
    return True