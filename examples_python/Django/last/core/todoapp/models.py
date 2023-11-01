from django.db import models
import datetime
from django.contrib.auth.models import User 

class Categorie(models.Model):
    default_cat = 'normal Categorie'
    cat_title = models.CharField(default=default_cat,max_length=100,auto_created=True)
    

    def __str__(self) :
        return self.cat_title

   
        

class Task(models.Model):
    crucial = 'crucial'
    important = 'important'
    normal = 'normal'
    not_urgent = 'not urgent'
    unimportant = 'unimportant'
    priorities=[
        (crucial,'Crucial'),
        (important, 'İmportant'),
        (normal, 'Normal'),
        (not_urgent,'Not Urgent'),
        (unimportant, 'Unimportant')
    ]
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='categories')
    title=models.CharField(max_length=25,default='Enter Title',blank=True)
    priority = models.CharField(
        max_length=20,
        choices=priorities,
        default=normal
    )
    content=models.TextField(max_length=300,default='Enter Task',blank=True)
    startingDate= models.DateTimeField (default=datetime.datetime.now(),blank=True)
    endDate= models.DateTimeField(blank=True)
    isActive=models.BooleanField(blank=True)
    
    def __str__(self):
        return self.title

