from typing import Any

from ninja_extra import route, ControllerBase, api_controller

from pkg.schemas.common import CommonOut
from pkg.schemas.typehint import RequestWithTenantType


@api_controller("/base/")
class BaseAppController(ControllerBase):
    @route.get("", response=[(200, Any), (404, CommonOut)], url_name="get")
    async def get(self, request: RequestWithTenantType):
        return {"hello": "world"}
