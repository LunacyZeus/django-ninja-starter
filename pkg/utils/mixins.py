from django.views.generic.base import ContextMixin


class CommonMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['number'] = random.randrange(1, 100)
        return context
