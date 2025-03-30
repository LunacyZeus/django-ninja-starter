from ninja_extra import NinjaExtraAPI

ninja_api = NinjaExtraAPI(
    title="Ninja Starter API",
    description="数据",
    urls_namespace="starter",
)
ninja_api.auto_discover_controllers()
