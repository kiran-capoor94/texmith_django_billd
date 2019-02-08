"""
Basic Product Manager. This model stores information regarding the
products added by the Admin. Includes information like:
1. Name of the Product
2. Price of the Product
3. Variant of the Product
4. Type of the Product
"""

from django.db import models
from django.conf import settings
# from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from djmoney.models.fields import MoneyField
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices

# User Model pulled from the settings.py file
# Always set AUTH_USER_MODEL using the settings file

User = settings.AUTH_USER_MODEL

MIN_STOCK = settings.MINIMUM_STOCK


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Product(models.Model):
    """
    Model to store the data relating to product. The Product Model is
    connected to the Variant Model and the Type model using M2M Relation.
    Basic Idea is that every product will have type and every type will
    have a variant under it, so Variant is indirectly inherited from the Type Table.

    And this functionality shall be added in a later update.
    Currently, a simple Product Model has been made. The Admin can add as
    many types and variants he wants, they won't be searchable or filterable etc.
    """
    # TODO: Add Product Type & Product Variant Feature in the App.
    STATUS = Choices(('draft', _('draft')), ('published', _('published')))
    name = models.CharField(_("Product Name"), max_length=150)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='INR', verbose_name=_('Price'))
    product_type = models.CharField(_("Product Type"), max_length=150, default='None')
    created = models.DateTimeField(_("Date Added"), auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(_("Date Last Edited"), auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=_("Manager Name"), on_delete=models.CASCADE)
    description = models.TextField(_("Product Description"), blank=True)
    status = StatusField()
    status_changed = MonitorField(monitor='status')
    published_at = MonitorField(monitor='status', when=['published'])

    # product_image =

    # tax_rate =
    # stock =

    objects = models.Manager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        # TODO: Add Indexing

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"pk": self.pk})


class StockQuerySet(models.QuerySet):
    def available(self):
        return self.filter(available=True)


class StockManager(models.Manager):
    def get_queryset(self):
        return StockQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().available()

    def get_by_id(self):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
        # TODO: Raise Error.

    # def available_stock_by_id(self):
    #     return self.get_by_id().filter()


class Stock(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Stock For Product"), on_delete=models.CASCADE)
    available = models.BooleanField(_("Available or Not"), default=True)
    available_stock = models.PositiveIntegerField(_("Stock Available"))
    sold = models.PositiveIntegerField(_("Stock Sold"))
    stock_changed = MonitorField(monitor='available')
    made_available_at = MonitorField(monitor='available', when=True)

    objects = StockManager()

    class Meta:
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Stock_detail", kwargs={"pk": self.pk})
