# Create your views here.
from django.shortcuts import render
from rest_framework import generics, permissions
from prosyndic import models as pro_models
from prosyndic import serializers as pro_seriz
# from prosyndic.permissions import IsAuthorOrReadOnly

# Residence
class ResidenceApiList(generics.ListCreateAPIView):
    serializer_class = pro_seriz.ResidenceApiSerializer 
    queryset = pro_models.Residence.objects.all().order_by('name')

class ResidenceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = pro_models.Residence.objects.all().order_by('name')
    serializer_class = pro_seriz.ResidenceApiSerializer 
    

# Appartement
class AppartementApiList(generics.ListCreateAPIView):
    serializer_class = pro_seriz.AppartementApiSerializer 
    queryset = pro_models.Appartement.objects.all().order_by('numero')

class AppartementDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = pro_models.Appartement.objects.all().order_by('numero')
    serializer_class = pro_seriz.AppartementApiSerializer 
    
# Incident
class IncidentApiList(generics.ListCreateAPIView):
    serializer_class = pro_seriz.IncidentApiSerializer 
    queryset = pro_models.Incident.objects.all().order_by('title')

class IncidentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = pro_models.Incident.objects.all().order_by('title')
    serializer_class = pro_seriz.IncidentApiSerializer 

# Proprietaire
class ProprietaireApiList(generics.ListCreateAPIView):
    serializer_class = pro_seriz.ProprietaireApiSerializer 
    queryset = pro_models.Proprietaire.objects.all().order_by('name')

class ProprietaireDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = pro_models.Proprietaire.objects.all().order_by('name')
    serializer_class = pro_seriz.ProprietaireApiSerializer 



# Document
class DocumentApiList(generics.ListCreateAPIView):
    serializer_class = pro_seriz.DocumentApiSerializer 
    queryset = pro_models.Document.objects.all().order_by('-id')

class DocumentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = pro_models.Document.objects.all().order_by('-id')
    serializer_class = pro_seriz.DocumentApiSerializer 


