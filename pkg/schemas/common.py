from collections import OrderedDict
from typing import (
    Any,
    List,
    Generic,
)

from ninja_extra.schemas.response import T
from pydantic import BeforeValidator, TypeAdapter, field_validator
from django.core.paginator import Page
from ninja import Field, Schema
from ninja.types import DictStrAny
from ninja_extra.pagination import PageNumberPaginationExtra


class CommonOut(Schema):
    msg: str


class BaseNinjaResponseSchema(Schema):
    items: List[Any]
    total: int


class PaginationResponseSchema(BaseNinjaResponseSchema, Generic[T]):
    items: List[T]

    @field_validator("items", mode="before")
    def validate_items(cls, value: Any) -> Any:
        if value is not None and not isinstance(value, list):
            value = list(value)
        return value


class PageSizePagination(PageNumberPaginationExtra):
    class Input(Schema):
        page: int = Field(1, gt=0)
        page_size: int = Field(100, lt=200)

    page_query_param = "page"
    page_size_query_param = "pageSize"

    max_page_size = 200

    def get_paginated_response(self, *, base_url: str, page: Page) -> DictStrAny:
        return OrderedDict(
            [
                ("total", page.paginator.count),
                ("items", list(page)),
            ]
        )
