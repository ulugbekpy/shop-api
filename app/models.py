from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    featured_product = models.ForeignKey('Product',
                                         on_delete=models.SET_NULL, null=True, related_name='collections')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']


class Customer(models.Model):
    MEMBERSHIP_CHOICES = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES)


class Order(models.Model):
    PENDING_PAYMENT_CHOICE = 'P'
    COMPLETED_PAYMENT_CHOICE = 'C'
    FAILED_PAYMENT_CHOICE = 'F'

    PAYMENT_CHOICES = [
        (PENDING_PAYMENT_CHOICE, 'Pending'),
        (COMPLETED_PAYMENT_CHOICE, 'Completed'),
        (FAILED_PAYMENT_CHOICE, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES)
