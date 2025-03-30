from django.db import models
from django.utils import timezone

from apps.demo import const


class CustomManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)


class Group(models.Model):
    name = models.CharField(
        verbose_name="分组名", default="分组名", max_length=32
    )  # 分组名
    alias = models.CharField(
        verbose_name="别名",
        default="别名",
        max_length=32,
        blank=True,
        unique=True,
    )
    remark = models.CharField(
        verbose_name="备注", default="备注", max_length=32, blank=True
    )  # 备注
    created = models.DateTimeField(
        verbose_name="创建时间", default=timezone.now, blank=True, null=True
    )
    # 使用自定义管理器
    objects = CustomManager()

    class Meta:
        verbose_name = "分组"
        verbose_name_plural = "分组"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name}"
