from django import forms
from learnCSS.models import Html


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
