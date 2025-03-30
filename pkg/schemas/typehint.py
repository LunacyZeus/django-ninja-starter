from django_hint import RequestType


class RequestWithTenantType(RequestType):
    tenant: any
