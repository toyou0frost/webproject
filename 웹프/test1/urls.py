from django.contrib import admin
from django.urls import path, include
from testapp1 import views

app_name = 'apptest'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apptest/', include('testapp1.urls')),
    path('common/', include('common.urls')),
    path('learnCSS/', include('learnCSS.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]
