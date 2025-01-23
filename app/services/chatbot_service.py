
from app.db import chatbot_db
from app.schema.chatbot_schema import ChatbotIn

async def get_chatbot_by_id(chatbot_id: str):
    return await chatbot_db.get_chatbot_by_id(chatbot_id)

async def get_all_chatbots_by_owner(owner_id: str):
    return await chatbot_db.get_all_chatbots_by_owner(owner_id)

async def create_chatbot(chatbot: ChatbotIn):
    return await chatbot_db.save_chatbot(chatbot)

async def update_chatbot(chatbot: ChatbotIn):
    return await chatbot_db.update_chatbot(chatbot)

async def delete_chatbot(chatbot_id: str):
    return await chatbot_db.delete_chatbot(chatbot_id)
