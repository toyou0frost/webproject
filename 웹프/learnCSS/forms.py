from django import forms
from learnCSS.models import Html,Html_Answer


class HtmlForm(forms.ModelForm):
    class Meta:
        model = Html # 사용할 모델
        fields = ['subject', 'html','css','content']
        labels = {
            'subject': '제목',
            'html': 'html',
            'css':'css',
            'content':'내용',
        }  
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Html_Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }