from abc import ABC, abstractmethod
from datetime import datetime

from src.values.date_format import DateFormat
from src.values.payments_dto import PaymentsDTO


class AbstractAggregatorRepo(ABC):

    @abstractmethod
    async def aggregate_by_dates(self,
                                 start_date: datetime,
                                 end_date: datetime,
                                 format_date: DateFormat) -> PaymentsDTO:
        ...
