from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

admin.site.site_header = 'Your admin name'

# Register your models here.
class CustomerTagsAdmin(ImportExportModelAdmin):
    # ListView options 
    search_fields = ['name']
admin.site.register(CustomerTags, CustomerTagsAdmin)

class CustomerAdmin(ImportExportModelAdmin):
    # ListView options 
    search_fields = ['name','email','phone','featured','created_on','updated_on']
    list_filter = ['featured','created_on','updated_on']
    list_per_page = 100
    list_display = ['id','name','email','phone','featured','created_on','updated_on']
    list_editable = ['featured']

    # DetailView options
    autocomplete_fields = ['tags']
    # prepopulated_fields = {'slug': ('name',),}
    fieldsets = (
        (None, {
            'fields' : (
                ('name'),
                ('phone','email'),
                ('featured'),
                'tags',
            )
        }),
        ('Description', {
            'classes': ('collapse closed',), # Changed because of grapelli. Earlier 'collapse'
            'fields' : (
                'description',
            )
        }),
    )

admin.site.register(Customer, CustomerAdmin)

