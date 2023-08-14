
from rest_framework import serializers
from prosyndic import models as pro_models

class ResidenceApiSerializer(serializers.ModelSerializer):
    class Meta :
        model = pro_models.Residence
        #fields = ('id', 'name', 'photo', 'comment',)
        fields = '__all__'
   
class AppartementApiSerializer(serializers.ModelSerializer):
    class Meta :
        model = pro_models.Appartement
        fields = '__all__'
   

class IncidentApiSerializer(serializers.ModelSerializer):
    class Meta :
        model = pro_models.Incident
        fields = '__all__'
        #fk_name = "Incident"
   
# Proprietaire
class ProprietaireApiSerializer(serializers.ModelSerializer):
    class Meta :
        model = pro_models.Proprietaire
        fields = '__all__'

# Document
class DocumentApiSerializer(serializers.ModelSerializer):
    class Meta :
        model = pro_models.Document
        fields = '__all__'
   