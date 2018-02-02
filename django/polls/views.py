from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    # 바로 render
    return render(request, 'polls/index.html', context )

    # 템플릿 로드후 응답
    # template = loader.get_template('poll/index.html')
    # return HttpResponse(template.render(context, request))

    # 일반 텍스트로 응답
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')

    # 위 처럼 처리하거나 아래 처럼

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
