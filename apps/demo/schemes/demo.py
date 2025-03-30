from typing import Optional, List
from ninja_schema import Schema


class HelloOut(Schema):
    msg: str
