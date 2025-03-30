"""
from django.core.exceptions import DisallowedHost
from django.db import connection
from django.http import Http404
from django_tenants.middleware import TenantMainMiddleware
from django_tenants.utils import get_tenant_domain_model
from django_tenants.utils import remove_www_and_dev, get_public_schema_urlconf


#多租户配置中间件
class TenantTutorialMiddleware(TenantMainMiddleware):
    def no_tenant_found(self, request, hostname):
        hostname_without_port = remove_www_and_dev(request.get_host().split(':')[0])
        if hostname_without_port in ("127.0.0.1", "localhost"):
            request.urlconf = get_public_schema_urlconf()
            return
        else:
            raise Http404

    def get_tenant(self, domain_model, hostname):
        #print('hostname', hostname)
        domain = domain_model.objects.select_related('tenant').get(domain=hostname)
        #print('tenant', domain.tenant)
        return domain.tenant
"""
