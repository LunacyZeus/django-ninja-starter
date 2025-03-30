from ninja_extra import route, ControllerBase, api_controller

from apps.demo.schemes.demo import HelloOut
from apps.demo.services.demo import hello


@api_controller("/demo/")
class DemoController(ControllerBase):
    @route.get("", response={200: HelloOut})
    def hello(self, user: str):
        out = hello(user)

        return out
