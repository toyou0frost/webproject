from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Html
from .forms import HtmlForm
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    """
    pybo 목록출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Html.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'learnCSS/index.html', context)

def codeEditor(request):
    html_content=Html_content.objects.all()
    return render(request, 'learnCSS/codeEditor.html',{'html_content':html_content})

# Create your views here.
def html_create(request):
    if request.method == 'POST':
        form = HtmlForm(request.POST)
        if form.is_valid():
            html = form.save(commit=False)
            html.author = request.user  # author 속성에 로그인 계정 저장
            html.create_date = timezone.now()
            html.save()
            return redirect('learnCSS:index')
    else:
        form = HtmlForm()
    context = {'form': form}
    return render(request, 'learnCSS/html_create.html', context)

def detail(request, html_id):
    question = Html.objects.get(id=html_id)
    context = {'question': question}
    return render(request, 'apptest/detail.html', context)
