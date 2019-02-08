from django.utils import timezone
from django.views.generic import ListView, DetailView

from .models import Product
from .forms import ProductAddForm


class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["published_at"] = timezone.now()
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductAddForm()
        return context
