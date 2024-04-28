from datetime import datetime, timedelta

from motor.motor_asyncio import AsyncIOMotorCollection

from src.abstracts.abstract_aggregator_repo import AbstractAggregatorRepo
from src.values.payments_dto import PaymentsDTO
from src.values.date_format import DateFormat


class AggregatorRepo(AbstractAggregatorRepo):

    def __init__(self, coll: AsyncIOMotorCollection) -> None:
        self._coll = coll

    async def aggregate_by_dates(self,
                                 start_date: datetime,
                                 end_date: datetime,
                                 format_date: DateFormat) -> PaymentsDTO:
        end_date_adjusted = end_date + timedelta(milliseconds=1)
        pipeline = [
            {
                '$match': {
                    'dt': {
                        '$gte': start_date,
                        '$lte': end_date
                    }
                }
            },
            {
                '$densify': {
                    'field': 'dt',
                    'range': {
                        'step': 1,
                        'unit': format_date.date_unit,
                        'bounds': [
                            start_date,
                            end_date_adjusted
                        ]
                    },
                }
            },
            {
                '$group': {
                    '_id': {
                        '$dateToString': {
                            'format': format_date.date_format,
                            'date': '$dt'
                        }
                    },
                    'dataset': {
                        '$sum': {
                            '$cond': {
                                'if': {'$eq': ['$value', None]},
                                'then': 0,
                                'else': '$value'
                            }
                        }
                    }
                }
            },
            {
                '$sort': {'_id': 1}
            },
            {
                '$group': {
                    '_id': None,
                    'labels': {'$push': '$_id'},
                    'dataset': {'$push': '$dataset'}
                }
            },
            {
                '$unset': '_id'
            },
        ]

        res = await self._coll.aggregate(pipeline).next()
        return PaymentsDTO.model_validate(res)
