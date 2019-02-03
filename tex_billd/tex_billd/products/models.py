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

# User Model pulled from the settings.py file
# Always set AUTH_USER_MODEL using the settings file

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    """
    Model to store the data relating to product. The Product Model is
    connected to the Variant Model and the Type model using M2M Relation.
    Basic Idea is that every product will have type and every type will
    have a variant under it, so Variant is indirectly inherited from the Type Table.

    And this functionality shall be added in a later update.
    Currently, a simple Product Model has been made, and the Admin can add as
    many types and variants he wants, they won't be searchable or filterable etc.
    """
    # TODO: Add Product Type & Product Variant Feature in the App.
    name = models.CharField(_("Prodcut Name"), max_length=150)
    price = models.PositiveIntegerField(_("Product Price"))
    product_type = models.CharField(_("Product Type"), max_length=150, default='None')
    created = models.DateTimeField(_("Date Added"), auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(_("Date Last Edited"), auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=_("Manager Name"), on_delete=models.CASCADE)
    description = models.TextField(_("Product Description"), blank=True)
    # tax_rate =

    objects = models.Manager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"pk": self.pk})
