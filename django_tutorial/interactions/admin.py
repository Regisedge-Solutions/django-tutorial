from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

admin.site.site_header = 'Your admin name'

# Register your models here.
class InteractionTypeAdmin(ImportExportModelAdmin):
    # ListView options 
    search_fields = ['name']
    list_per_page = 100
    list_display = ['id','name']

admin.site.register(InteractionType, InteractionTypeAdmin)

class InteractionSubTypeAdmin(ImportExportModelAdmin):
    # ListView options 
    search_fields = ['name','interaction_type']
    list_per_page = 100
    list_display = ['id','name','interaction_type']

    # DetailView options
    autocomplete_fields = ['interaction_type']

admin.site.register(InteractionSubType, InteractionSubTypeAdmin)





class DispositionAdmin(ImportExportModelAdmin):
    # ListView options 
    search_fields = ['name']
    list_per_page = 100
    list_display = ['id','name']

admin.site.register(Disposition, DispositionAdmin)

class SubdispositionAdmin(ImportExportModelAdmin):
    # ListView options 
    search_fields = ['name']
    list_per_page = 100
    list_display = ['id','name','disposition']

    # DetailView options
    autocomplete_fields = ['disposition']

admin.site.register(Subdisposition, SubdispositionAdmin)






class InteractionAdmin(ImportExportModelAdmin):
    # ListView options 
    search_fields = ['customer']
    list_filter = ['follow_up','follow_up_date','interaction_subtype','subdisposition','created_on','updated_on']
    list_per_page = 100
    list_display = ['customer','interaction_subtype','subdisposition','follow_up','follow_up_date','created_on','updated_on']
    list_editable = ['follow_up','follow_up_date']

    # DetailView options
    autocomplete_fields = ['customer','interaction_subtype','subdisposition']
    # prepopulated_fields = {'slug': ('name',),}
    fieldsets = (
        (None, {
            'fields' : (
                ('customer'),
                ('interaction_subtype','subdisposition'),
                ('follow_up','follow_up_date'),
                'description',
            )
        }),
    )

admin.site.register(Interaction, InteractionAdmin)
