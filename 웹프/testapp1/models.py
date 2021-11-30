from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    create_date = models.DateTimeField(null=True)