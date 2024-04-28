from functools import lru_cache
from typing import Literal


@lru_cache
def get_format_date_by_mode(mode: Literal['month', 'day', 'hour']) -> str:
    converter = {
        'month': '%Y-%m-01T00:00:00',
        'day': '%Y-%m-%dT00:00:00',
        'hour': '%Y-%m-%dT%H:00:00'
    }
    return converter[mode]
