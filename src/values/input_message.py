from pydantic import BaseModel, Field


class InputMessage(BaseModel):

    dt_from: str = Field(pattern=r'^[0-9]{4}-(0[0-9]|1[012])-([0-2][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
    dt_upto: str = Field(pattern=r'^[0-9]{4}-(0[0-9]|1[012])-([0-2][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
    group_type: str
