from django.contrib import admin
from django.urls import path, include
from prosyndic import views as pro_view

urlpatterns = [
    path('',  pro_view.IncidentApiList.as_view(), ), # new
    # Residence
    path('residence/<int:pk>/',  pro_view.ResidenceDetails.as_view(), ), # new
    path('residence/',  pro_view.ResidenceApiList.as_view(), ), # new
    
    # appartement
    path('appart/<int:pk>/',  pro_view.AppartementDetails.as_view(), ), # new
    path('appart/',  pro_view.AppartementApiList.as_view(), ), # new
    
    # incident
    path('incident/<int:pk>/',  pro_view.IncidentDetails.as_view(), ), # new
    path('incident/',  pro_view.IncidentApiList.as_view(), ), # new

    # Proprietaire
    path('prop/<int:pk>/',  pro_view.ProprietaireDetails.as_view(), ), # new
    path('prop/',  pro_view.ProprietaireApiList.as_view(), ), # new

    # Document
    path('doc/<int:pk>/',  pro_view.DocumentDetails.as_view(), ), # new
    path('doc/',  pro_view.DocumentApiList.as_view(), ), # new
]