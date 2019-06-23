from django.db import models

# Create your models here.
class Disorder(models.Model):
    title = models.CharField(max_length=100) #Title of Disorder
    slug = models.SlugField() #Use to create URLs
    body = models.TextField() #Details of Disorder
    
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[0:50] + '...'
    