from aiogram import Router, F
from aiogram.types import Message
from typing import Any
import json

from src.config import get_settings
from src.values.input_message import InputMessage
from src.repos.aggregator_repo import AggregatorRepo
from src.services.get_aggregated_data import GetAggregatedDataService
from src.db import client

default_router = Router()


@default_router.message(F.text)
async def default_handler(message: Message) -> Any:
    settings = get_settings()

    input_message = InputMessage.model_validate(json.loads(message.text))

    repo = AggregatorRepo(client[settings.MONGO_NAME][settings.MONGO_COLL])
    service = GetAggregatedDataService(repo=repo)

    payments = await service.get_aggregated_data(message=input_message)

    await message.answer(str(payments))
