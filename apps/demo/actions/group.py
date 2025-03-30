# Register your models here.


def unset_is_use(modeladmin, request, queryset):
    queryset.update(is_use=False)


unset_is_use.short_description = "批量取消使用"


def unset_is_return(modeladmin, request, queryset):
    queryset.update(is_return=False)


unset_is_return.short_description = "批量取消返回"


def set_is_use(modeladmin, request, queryset):
    queryset.update(is_use=True)


set_is_use.short_description = "批量设置使用"


def set_is_return(modeladmin, request, queryset):
    queryset.update(is_return=True)


set_is_return.short_description = "批量设置返回"


def set_black(modeladmin, request, queryset):
    queryset.update(is_lh=True)


set_black.short_description = "批量设置拉黑"
