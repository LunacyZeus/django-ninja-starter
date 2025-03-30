from pkg.response.response import APIResponse


def index_view(request):
    return APIResponse(code=0, msg="success")
