from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.auth.models import User
import django
from django.conf import settings

now = django.utils.timezone.now()


# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length = 100)
    jfile = models.FileField(upload_to='upload/', blank=True, null=True)
   
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def create_relation(self, obj):
        """
        in : obj 
        out : 
        """
        self.content_object = obj
        self.save()

    def get_document_or_object(self, obj, distinction=None):
        """
        This function allows you to get pieces for a specific object
        If distinction is set it will filter out any relation that doesnt have
        that distinction.
        
        >>> user = User.objects.get(username='tony')
        >>> try:
        ...     Piece.objects.get_piece_for_object(user)
        ... except Piece.DoesNotExist:
        ...     print("failed")
        ...
        failed
        Now if we add a piece it should return the piece
        >>> piece = Piece(name='My Cal')
        >>> piece.save()
        >>> piece.create_relation(user)
        >>> Piece.objects.get_piece_for_object(user)
        <Piece: My Cal>
        """
        ct = ContentType.objects.get_for_model(obj)
        return ct
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    class Meta:
        indexes = [ models.Index(fields=["content_type", "object_id"]), ]
   
class Residence(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media/")
    adresse = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(null=True)

    class Meta:
        verbose_name = _('Residence')
        verbose_name_plural = _('Residences')
        ordering = ('name',)
    
    def __unicode__(self):
        return u'%s' % self.name
    def __str__(self):
        return u'%s' % self.name

class Proprietaire(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Proprietaire')
        ordering = ('name',)
    
    def __unicode__(self):
        return u'%s' % self.name
    def __str__(self):
        return u'%s' % self.name


class Appartement(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    propriotaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    numero = models.SmallIntegerField(null=True)
    lot    = models.SmallIntegerField(null=True)
    etage  = models.SmallIntegerField(null=True)

    class Meta:
        verbose_name = _('Appartement')
        ordering = ('numero',)
    
    def __unicode__(self):
        return u'%s' % self.numero
    def __str__(self):
        return u'%s' % self.numero


class Incident(models.Model):
    title = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Piece jointe
    documents  = GenericRelation(Document)

    def add_document(self, piecej):
        self.documents.add(piecej, bulk=False)
        return True

    def documents_join(self):
        return self.documents.all()


    class Meta:
        verbose_name = _('Incident')
        verbose_name_plural = _('Incidents')
        ordering = ('-created_at',)
        
    
    def __unicode__(self):
        return u'%s' % self.title
    def __str__(self):
        return u'%s' % self.title




