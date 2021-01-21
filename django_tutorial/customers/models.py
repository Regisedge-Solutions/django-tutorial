from django.db import models

class CustomerTags(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "1. Customer Tags" 
        verbose_name = "Customer Tag"
        ordering = ('name',)

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    description = models.TextField(max_length=200, null=True, blank=True)
    featured = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    tags = models.ManyToManyField(CustomerTags)

    def __str__(self):
        return f'{self.name} ({self.email})' or ''

    @property
    def display_name(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name_plural = "2. Customers" 
        verbose_name = "Customer"
        ordering = ('name',)
