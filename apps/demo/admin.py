from django.contrib import admin
from application.admin import admin_site
from . import models
from .actions.group import (
    unset_is_use,
    unset_is_return,
    set_is_use,
    set_is_return,
)


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "alias",
        "remark",
        "created",
    )
    search_fields = ("name",)
    list_filter = ("created",)
    actions = [unset_is_use, unset_is_return, set_is_use, set_is_return]


admin_site.register(models.Group, GroupAdmin)
