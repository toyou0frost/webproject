from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Html, Html_Answer
from .forms import HtmlForm, AnswerForm
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
    html_list = Html.objects.order_by('-create_Date')

    # 페이징처리
    paginator = Paginator(html_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'html_list': page_obj}
    return render(request, 'learnCSS/index.html', context)

def codeEditor(request):
    return render(request, 'learnCSS/codeEditor.html')

# Create your views here.
def html_create(request):
    if request.method == 'POST':
        form = HtmlForm(request.POST)
        if form.is_valid():
            html = form.save(commit=False)
            html.author = request.user  # author 속성에 로그인 계정 저장
            html.create_Date = timezone.now()
            html.save()
            return redirect('learnCSS:index')
    else:
        form = HtmlForm()
    context = {'form': form}
    return render(request, 'learnCSS/html_create.html', context)

def detail(request, question_id):
    question = Html.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'learnCSS/learnCSS_detail.html', context)

@login_required(login_url='common:login')
def html_answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Html, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_Date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('learnCSS:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'learnCSS/learnCSS_detail.html', context)  

@login_required(login_url='common:login')
def html_question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = HtmlForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_Date = timezone.now()
            question.save()
            return redirect('learnCSS:index')
    else:
        form = HtmlForm()
    context = {'form': form}
    return render(request, 'learnCSS/html_create.html', context)


@login_required(login_url='common:login')
def html_question_modify(request, question_id):
    """
    pybo 질문수정
    """
    question = get_object_or_404(Html, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('learnCSS:detail', question_id=question.id)

    if request.method == "POST":
        form = HtmlForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_Date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('learnCSS:detail', question_id=question.id)
    else:
        form = HtmlForm(instance=question)
    context = {'form': form}
    return render(request, 'learnCSS/html_create.html', context)

@login_required(login_url='common:login')
def html_question_delete(request, question_id):
    """
    pybo 질문삭제
    """
    question = get_object_or_404(Html, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('learnCSS:detail', question_id=question.id)
    question.delete()
    return redirect('learnCSS:index')

@login_required(login_url='common:login')
def html_answer_modify(request, answer_id):
    """
    pybo 답변수정
    """
    answer = get_object_or_404(Html_Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('learnCSS:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_Date = timezone.now()
            answer.save()
            return redirect('learnCSS:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'learnCSS/answer_form.html', context)

@login_required(login_url='common:login')
def html_answer_delete(request, answer_id):
    """
    pybo 답변삭제
    """
    answer = get_object_or_404(Html_Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('learnCSS:detail', question_id=answer.question.id)