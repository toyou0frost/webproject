from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

# Create your models here.
class Html(models.Model):
    subject = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    css = models.TextField(null=True)
    html = models.TextField(null=True)
    content = models.TextField(null=True)
    # create_date = models.DateTimeField(auto_now_add=True)
    # modify_date = models.DateTimeField(null=True, blank=True)

    create_Date = models.DateTimeField(null=True)
    modify_Date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject
        
class Html_Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    question = models.ForeignKey(Html, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    modify_Date = models.DateTimeField(null=True, blank=True)
    create_Date = models.DateTimeField()