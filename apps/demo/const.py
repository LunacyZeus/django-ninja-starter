from django.db import models
from django.utils.translation import gettext_lazy as _


class TestChoices(models.TextChoices):
    American = "American", _("美国")
    Canada = "Canada", _("加拿大")
    HongKong = "HongKong", _("香港")
    China = "China", _("中国")
    Ukraine = "Ukraine", _("乌克兰")
