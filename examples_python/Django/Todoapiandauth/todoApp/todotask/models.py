from django.db import models
import datetime
from django.contrib.auth.models import User 
# Create your models here.
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
    task_cat = models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='categories')
    task_title=models.CharField(max_length=25,default='Enter Title',blank=True)
    priority = models.CharField(
        max_length=20,
        choices=priorities,
        default=normal
    )
    task_content=models.TextField(max_length=300,default='Enter Task',blank=True)
    task_startingDate= models.DateTimeField (default=datetime.datetime.now(),blank=True)
    task_endDate= models.DateTimeField(blank=True)
    task_isActive=models.BooleanField(blank=True)
    # remaining_time=models.DateTimeField(
    #     read_only = True
    #     default=startingDate-endDate
    # 

    def __str__(self):
        return self.task_title



# class Regusermodel(AbstractUser):
    
#     username_validator = UnicodeUsernameValidator()
#     username = models.CharField(
#         str("username"),
#         max_length=150,
#         unique=True,
#         validators=[username_validator],
#         error_messages={
#             "unique": str("A user with that username already exists."),
#         },
#     )
#     first_name = models.CharField(str("first name"), max_length=150, blank=True)
#     last_name = models.CharField(str("last name"), max_length=150, blank=True)
#     email = models.EmailField(str("email address"), blank=True)
#     is_staff = models.BooleanField(
#         str("staff status"),
#         default=False,
#     )
#     is_active = models.BooleanField(
#         str("active"),
#         default=True,
        
#     )





