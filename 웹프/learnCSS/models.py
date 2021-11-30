from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
class Html(models.Model):
    subject = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    css = models.TextField(null=True)
    html = models.TextField(null=True)
    content = models.TextField(null=True)
    # create_date = models.DateTimeField(default=datetime.datetime.now)
    # modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.subject

def now():
    """
    Returns an aware or naive datetime.datetime, depending on settings.USE_TZ.
    """
    if settings.USE_TZ:
        # timeit shows that datetime.now(tz=utc) is 24% slower
        return datetime.utcnow().replace(tzinfo=utc)
    else:
        return datetime.now()