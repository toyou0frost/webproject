from django.urls import path
from . import views

app_name = 'learnCSS'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('codeEditor/', views.codeEditor, name='codeEditor'),
    path('htmlanswer/create/<int:question_id>/', views.html_answer_create, name='html_answer_create'),
    path('htmlquestion/create/', views.html_create, name='html_create'),
    path('htmlquestion/modify/<int:question_id>/', views.html_question_modify, name='html_question_modify'),
    path('htmlquestion/delete/<int:question_id>/', views.html_question_delete, name='html_question_delete'),
    path('htmlanswer/modify/<int:answer_id>/', views.html_answer_modify, name='html_answer_modify'),
    path('htmlanswer/delete/<int:answer_id>/', views.html_answer_delete, name='html_answer_delete'),
]