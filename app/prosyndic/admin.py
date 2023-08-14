from django.contrib import admin
from prosyndic import models as pro_models

# Register your models here.

class ResidenceAdmin(admin.ModelAdmin):
    list_display  = ('name', 'adresse', 'comment')
    # list_display  = [f.name for f in pro_models.Residence._meta.get_fields()]
    # search_fields = ['name',]
    fk_name = "appartement"


class ProprietaireAdmin(admin.ModelAdmin):
    list_display  = ('name', )
  
class AppartementAdmin(admin.ModelAdmin):
    list_display  = ('residence', 'lot', 'etage', )

class IncidentAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in pro_models.Incident._meta.get_fields()]
    list_display  = ('title', 'comment',  'created_at', 'get_author', 'get_documents', )
    #list_select_related = ('author',  )
    search_fields = ['title',]
    
    def get_author(self, obj):
        return obj.author.username
    
    def get_documents(self, obj):
        return obj.documents.all().first()



  
# annonce
admin.site.register(pro_models.Residence, ResidenceAdmin)
admin.site.register(pro_models.Proprietaire, ProprietaireAdmin)
admin.site.register(pro_models.Appartement, AppartementAdmin)
admin.site.register(pro_models.Incident, IncidentAdmin)