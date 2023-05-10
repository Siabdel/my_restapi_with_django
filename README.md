# my_restapi_with_django
My Rest Api with django rest Framework

![projet](/home/django/Depots/mesdoc_md/Vuejs/images/vuejs.png)





#  Rest APIs with Django Framework



>  **Créer des APIs web avec Django Rest Framework**
>
>  3 points a mettre en place 
>
>  * a **urls.py** pour les urls routes
>  * a **serializes.py** pour transformer les data en **JSON**
>  * a views.py fichier pour appliquer la logic de chaque **API endpoints**
>
>  



## la configuration initiale



```shell
$ mkvirtualenv envBlogApi && cdvirtualenv
# install Django
$ pip install django
# creation du projet blogapi
$ django-admin startproject blogapi && cd blogapi
# start application
$ ./manage.py startapp blog



```



Maintenant nous allons utiliser **Django REST Framework**

## DjangoRestFrameWork install

```shell
$ pip install djangorestframework
```



## Settings

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'blog.apps.BlogConfig',
   # Django Rest Framework - 3 rd party apps
    'rest_framework', # new
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.AllowAny',
    ]
}
```



## migrate 

```shell
$ ./manage.py migrate 
$ ./manage.py createsuperuser
```



## Models 

```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogApi(models.Model):
    author  = models.ForeignKey('User', on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    body    = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.title
```



## migrate models

```shell
$ ./manage.py makemigrations blog
$ ./manage.py migrate
```



## URLS

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',  include('blog.urls')), # new
]
```



## Serializers 



Creer un nouveau fichier serializers.py pour notre applications blogapi



```python
# postapi/serializers.py

from rest_framework import serializers
from .models import BlogApi

class PostApiSerializer(serializers.ModelSerializer):
    class Meta :
        fields = ('id', 'title', 'body', 'created_at', )
        models = BlogApi
    
```



## Views

Notre controleur views .



```python
from django.shortcuts import render
# Create your views here.

# postapi/views.py
from rest_framework import generics
from .models import BlogApi
from .serilizers import PostApiSerializer 


class PostList(generics.ListCreateAPIView):
    serializer_class = PostApiSerializer
    queryset = BlogApi.objects.all()
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogApi.objects.all()
    serilizer_class = PostApiSerializer
    
    
```

## Git Deploy sources



```shell
$ git init 
$ git Branch -m main
# remote add 
$ git remote add  origin https://github.com/Siabdel/my_restapi_with_django.git
$ git pull origin main 
$ git push origin main 
# add src 
$ git add .
$ git commit -am "init project blogapi my restapi with django"
```





## Tests 

```python
from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User 

from .models import BlogApi 

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        
        # create a blog post 
        test_post = BlogApi.objects.create(
            author=testuser1, title='Blog title', body='Body content...')
        test_post.save()
        
    def test_post_content(self):
        post = BlogApi.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'

        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'Blog title')
        self.assertEqual(expected_body, 'Body content...')
        
```



pour confirmer que le test marche on lance la commande ligne 

```shell
$ python manage.py test
##
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.416s

OK
```





## Annexes 

CREATE TABLE "appipro_product" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL UNIQUE)

```python
$ ./manage.py dumpdata --format json --indent 2 appipro
$ ./manage.py sqlmigrate  appipro 0001_initial >> schema_001.sql
$ ./manage.py dumpdata -table users db/users.json
$ ./manage.py dumpdata -table django-users 
$ ./manage.py dumpdata  django-users 

$ CREATE TABLE "appipro_product" ("id" serial NOT NULL PRIMARY KEY);
```


