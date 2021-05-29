from django.db import models
from category.models import Category 
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_avalible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modifield_date = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse("store:product_detail", args=[self.product_slug])
    

    def __str__(self):
        return self.name

