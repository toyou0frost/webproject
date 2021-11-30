from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Html(models.Model):
    subject = models.CharField(max_length=200,null=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    css= models.TextField(null=True)
    html= models.TextField(null=True)
    content = models.TextField(null=True)
    # modify_date = models.DateTimeField(null=True, blank=True)
    # create_date = models.DateTimeField()
    def __str__(self):
        return self.subject
