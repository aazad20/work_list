from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null= True,blank = True )
    title = models.CharField(max_length=200)
    desc  = models.TextField(max_length=10000,blank=True,null=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
     

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['done']
