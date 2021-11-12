from django.shortcuts import render

def index(request):    
    return render(request, 'learnCSS/index.html')

def codeEditor(request):
    return render(request, 'learnCSS/codeEditor.html')
# Create your views here.
