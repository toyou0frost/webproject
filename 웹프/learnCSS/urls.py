from django.urls import path
from . import views

app_name = 'learnCSS'

urlpatterns = [
    path('', views.index, name='index'),
    path('codeEditor/', views.codeEditor, name='codeEditor'),
    path('html_create/', views.html_create, name='html_create'),
    path('<int:html_id>/', views.detail, name='detail'),
]