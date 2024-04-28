from pydantic import BaseModel, Field


class DateFormat(BaseModel):

    date_unit: str
    date_format: str = Field(pattern=r'''^(%Y|[0-9]{4})-(%m|0[0-9]|1[012])-(%d|[0-2][0-9]|3[01])T(%H|[01][0-9]|2[0-3]):(%M|[0-5][0-9]):(%S|[0-5][0-9])$''')
