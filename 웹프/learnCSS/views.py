from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Html
from .forms import HtmlForm

def index(request): 
    return render(request, 'learnCSS/index.html')

def codeEditor(request):
    html_content=Html_content.objects.all()
    return render(request, 'learnCSS/codeEditor.html',{'html_content':html_content})
# Create your views here.
def html_create(request):

    # if request.method == 'POST':
    #     form = HtmlForm(request.POST)
    #     if form.is_valid():
    #         html = form.save(commit=False)
    #         # html.author = request.user  # author 속성에 로그인 계정 저장
    #         # html.create_date = timezone.now()
    #         html.save()
    #         return redirect('learnCSS:index')
    # else:

    form = HtmlForm()
    context = {'form': form}
    return render(request, 'learnCSS/html_create.html', context)
