"""
URL configuration for blogapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('blog.urls')), # new
    path('api/v1/',  include('blog.urls')), # new
    path('api/v2/',  include('prosyndic.urls')), # new
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    # user registrations
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    
]

## Token  
urlpatterns += [ 
     path('token/create/', jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'), 
     path('token/refresh/', jwt_views.TokenRefreshView.as_view(), 
          name =' token_refresh'),
     path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify') 
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
