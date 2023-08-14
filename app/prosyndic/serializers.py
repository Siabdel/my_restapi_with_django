
from rest_framework import serializers
from prosyndic import models as pro_models
from django.conf import settings
from django.contrib.auth.models import User, Group, Permission

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'

# Document
class DocumentApiSerializer(serializers.ModelSerializer):
    class Meta :
        model = pro_models.Document
        #fields = '__all__'
        fields = ('content_type', 'object_id', 'title',)
   
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
    # author = serializers.StringRelatedField(many=False, read_only=True)
    # author = serializers.SerializerMethodField()
    author = UserSerializer()

    #documents = DocumentApiSerializer()
    documents = serializers.StringRelatedField(many=True, read_only=True)
    
    def get_author(self, obj):
        return obj.author.username
    

    class Meta :
        model = pro_models.Incident
        #fields = '__all__'
        fields  = ('title', 'comment',  'created_at', 'author', 'documents',  )
   
# Proprietaire
class ProprietaireApiSerializer(serializers.ModelSerializer):
    class Meta :
        model = pro_models.Proprietaire
        fields = '__all__'