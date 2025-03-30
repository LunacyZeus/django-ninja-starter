"""peer_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from application.admin import admin_site
from apps.api import ninja_api
from apps.demo.views import index_view

urlpatterns = [
    path("", index_view),
    path("index", index_view),
    path("api/", ninja_api.urls),
    path("admin/", admin_site.urls),
    # path("demo/", include("apps.demo.urls")),
]
