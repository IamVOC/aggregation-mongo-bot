import pytest
from unittest.mock import Mock, MagicMock
import asyncio

from src.values.payments_dto import PaymentsDTO
from src.values.input_message import InputMessage
from src.services.get_aggregated_data import GetAggregatedDataService


@pytest.mark.asyncio
async def test_get_aggregated_data():
    repo_res = PaymentsDTO(dataset=[0, 1],
                           labels=["2022-10-01T00:00:00",
                                   "2022-10-02T00:00:00"])
    f = asyncio.Future()
    f.set_result(repo_res)
    repo_mock = Mock()
    repo_mock.aggregate_by_dates = MagicMock(return_value=f)
    input_message = InputMessage(dt_from="2022-10-01T00:00:00",
                                 dt_upto="2022-10-02T00:00:00",
                                 group_type='day')
    service = GetAggregatedDataService(repo_mock)

    res = await service.get_aggregated_data(input_message)

    assert res == repo_res
