from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)

class Genrative_ai_data(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True, blank=True)
    data = models.TextField(null=True,blank=True)
    # date = models.DateField(_(""), auto_now=False, auto_now_add=False)