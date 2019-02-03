from django.utils import timezone
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["timestamp"] = timezone.now()
        return context
