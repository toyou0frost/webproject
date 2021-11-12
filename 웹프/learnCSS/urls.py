from django.urls import path
from . import views

app_name = 'learnCSS'

urlpatterns = [
    path('', views.index, name='index'),
    path('codeEditor/', views.codeEditor, name='codeEditor'),
]