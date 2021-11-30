from django.contrib import admin

# Register your models here.
from .models import Html, Html_Answer

admin.site.register(Html)
admin.site.register(Html_Answer)