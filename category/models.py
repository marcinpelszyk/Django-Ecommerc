from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(verbose_name=_('description'), help_text=_('Not Required'), max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='image/categories', blank=True)

    class  Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def get_absolute_url(self):
        return reverse('store:product_by_category', args=[self.slug])

    def __str__(self):
        return self.name

    