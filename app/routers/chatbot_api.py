from fastapi import APIRouter

from app.schema.chatbot_schema import ChatbotIn
from app.services import chatbot_service

router = APIRouter(prefix="/v1/chatbot")

@router.get('/{chatbotId}/{ownerId}')
async def get_chatbot_by_id(chatbot_id: str, owner_id: str):
    return await chatbot_service.get_chatbot_by_id(chatbot_id)

@router.get('/{ownerId}')
async def get_all_chatbots_by_owner(owner_id: str):
    return await chatbot_service.get_all_chatbots_by_owner(owner_id)

@router.post('/{ownerId}')
async def create_chatbot(chatbot: ChatbotIn, owner_id: str):
    return await chatbot_service.create_chatbot(chatbot)

@router.put('/{ownerId}')
async def update_chatbot(chatbot: ChatbotIn, owner_id: str):
    return await chatbot_service.update_chatbot(chatbot)

@router.delete('/{chatbotId}/{ownerId}')
async def delete_chatbot(chatbot_id: str, owner_id: str):
    return await chatbot_service.delete_chatbot(chatbot_id)