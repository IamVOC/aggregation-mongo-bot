from datetime import datetime

from src.abstracts.abstract_aggregator_repo import AbstractAggregatorRepo
from src.abstracts.abstract_get_aggregated_data import (
        AbstractGetAggregatedDataService
        )
from src.values.input_message import InputMessage
from src.values.payments_dto import PaymentsDTO
from src.values.date_format import DateFormat
from src.utils import get_format_date_by_mode


class GetAggregatedDataService(AbstractGetAggregatedDataService):

    def __init__(self, repo: AbstractAggregatorRepo) -> None:
        self._repo = repo

    async def get_aggregated_data(self,
                                  message: InputMessage) -> PaymentsDTO:

        group_format = get_format_date_by_mode(message.group_type)
        format_date = DateFormat(date_unit=message.group_type,
                                 date_format=group_format)

        start_date = datetime.fromisoformat(message.dt_from)
        end_date = datetime.fromisoformat(message.dt_upto)

        payments = await self._repo.aggregate_by_dates(start_date=start_date,
                                                       end_date=end_date,
                                                       format_date=format_date)

        return payments
