from django.db import models
from customers.models import * 


class InteractionType(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name}' or ''

    @property
    def display_name(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "2. Interaction Type" 


class InteractionSubType(models.Model):
    name = models.CharField(max_length=200, null=True)
    interaction_type = models.ForeignKey(InteractionType, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return f'{self.name} - {self.interaction_type}' or ''

    @property
    def display_name(self):
        return f'{self.name} - {self.interaction_type}'

    class Meta:
        verbose_name_plural = "3. Interaction Sub-Type" 

class Disposition(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name}' or ''

    @property
    def display_name(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "4. Dispositions" 

class Subdisposition(models.Model):
    name = models.CharField(max_length=200, null=True)
    disposition = models.ForeignKey(Disposition, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return f'{self.name} - {self.disposition}' or ''

    @property
    def display_name(self):
        return f'{self.name} - {self.disposition}'

    class Meta:
        verbose_name_plural = "5. Subdispositions" 


class Interaction(models.Model):    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL, blank=True)

    interaction_subtype = models.ForeignKey(InteractionSubType, null=True, on_delete= models.SET_NULL)
    subdisposition = models.ForeignKey(Subdisposition, null=True, on_delete= models.SET_NULL)

    description = models.TextField(max_length=200, null=True, blank=True)

    follow_up = models.BooleanField(default=False)
    follow_up_date = models.DateTimeField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'{self.customer} ({self.interaction_subtype})' or ''

    @property
    def display_name(self):
        return f'{self.customer} ({self.interaction_subtype})'

    # Can be used to change the display name on admin
    class Meta:
        verbose_name_plural = "1. Interactions" 
        verbose_name = "Interaction"
        ordering = ('created_on',)


