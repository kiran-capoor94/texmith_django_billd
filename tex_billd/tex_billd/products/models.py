"""
Basic Product Models & Managers. This model stores information regarding the
products added by the Admin. Includes information like:
1. Name of the Product
2. Price of the Product
3. Variant of the Product
4. Type of the Product

Includes Stock Models & manager, for basic
stock management.
"""

from django.db import models
from django.conf import settings
# from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from djmoney.models.fields import MoneyField
# from django_extensions.db.fields import AutoSlugField  # noqa
from model_utils.fields import MonitorField

# User Model pulled from the settings.py file
# Always set AUTH_USER_MODEL using the settings file
User = settings.AUTH_USER_MODEL


class StockQuerySet(models.QuerySet):
    def available(self):
        """
        Filter out all 'Not Available' Products from
        ``all()`` function.
        """
        return self.filter(available=True)


class StockManager(models.Manager):
    def get_queryset(self):
        return StockQuerySet(self.model, using=self._db)


class Stock(models.Model):
    """
    Stock Management is done by using the availabe_stock variable.
    Logic is if there are 10 BMW M3 GTRs in the inventory. After every
    purchase made the inventory/stock shall be reduced by the number of items sold.
    This logic is implemented in the views.py of the Products Component.
    """
    objects = models.StockManager()
    available_stock = models.PositiveIntegerField(_("Stock Available"), default=0)  # Available Stock
    stock_changed = MonitorField(monitor='available', verbose_name=_('Last Changed At'))

    class Meta:
        verbose_name = _("Stock")
        verbose_name_plural = _("Stocks")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Stock_detail", kwargs={"pk": self.pk})


class ProductQuerySet(models.QuerySet):
    pass


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        """
        Get all Available Products.
        """
        return self.get_queryset().available()

    def get_by_id(self):
        """
        Filter available products by ID.
        """
        qs = self.available().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
        # TODO: Raise Error.


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

    company_name = models.CharField(_("Product Company Name"), max_length=150, default='Company Name')
    name = models.CharField(_("Product Name"), max_length=150)
    serial_number = models.PositiveIntegerField(_("Product Serial Number"), blank=True, default=0)
    description = models.TextField(_("Product Description"), blank=True)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='INR', verbose_name=_('Price'))
    # product_type = models.CharField(_("Product Type"), max_length=150, default='None')

    # Monitor Fields
    created = models.DateTimeField(_("Date Added"), auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(_("Date Last Edited"), auto_now=False, auto_now_add=True)
    available = models.BooleanField(_("Product Availability"), default=False)  # Availability Status
    status_changed = MonitorField(monitor='available')
    available_at = MonitorField(monitor='available', when=[True])

    # Stock Model Connection
    stock = models.OneToOneField(Stock, verbose_name=_("Stock"), on_delete=models.CASCADE)

    # TODO: Add Auto_Slug Field
    slug = models.AutoSlugField(_("URL Slug for Product"), populate_from=[
                                'company_name', 'name', 'description'])

    # User Connection
    user = models.ForeignKey(User, verbose_name=_("Manager Name"), on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        # TODO: Add Indexing

    def __str__(self):
        return self.name

# TODO: Add Elastic Search of Google Search
# TODO: Add post_save Signal to check the stock and change the product from available to not available.
# TODO: Availabilty Mixin has to be added in the views directly.
