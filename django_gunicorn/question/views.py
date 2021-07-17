from django.shortcuts import render
from .models import Question
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
# Create your views here.

def question(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 1)
    page_number = request.GET.get('page') or 1
    page = Paginator.get_page(paginator, page_number)

    if int(page_number) <= questions.count():
        return render(request, 'question.html', {'page': page})
    else:
        return redirect('home')