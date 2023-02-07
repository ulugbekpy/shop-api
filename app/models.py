from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
