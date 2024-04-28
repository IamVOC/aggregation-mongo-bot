from abc import ABC, abstractmethod

from src.values.input_message import InputMessage
from src.values.payments_dto import PaymentsDTO


class AbstractGetAggregatedDataService(ABC):

    @abstractmethod
    async def get_aggregated_data(self,
                                  message: InputMessage) -> PaymentsDTO:
        ...
