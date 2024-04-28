from typing import List
from pydantic import BaseModel


class PaymentsDTO(BaseModel):
    dataset: List[int]
    labels: List[str]
