from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

templates = {
    'index': 'polls/index.html',
    'detail': 'polls/detail.html',
    'results': 'polls/results.html',
    'vote': 'polls/vote.html',
}

# Create your views here.
'''
    def index(req):
        lastest_questions = Question.objects.order_by('-pub_date')[:5]
        context = {
            'lastest_questions': lastest_questions,
        }
    
        return render(req, templates['index'], context)

    def detail(req, question_id):
        question = get_object_or_404(Question, pk=question_id)
        choices = question.choice_set.all()

        return render(req, templates['detail'], {'question': question, 'choices': choices})

    def results(req, question_id):
        question = get_object_or_404(Question, pk=question_id)
        choices = question.choice_set.all()

        return render(req, templates['results'], {'question': question, 'choices': choices})
'''

class IndexView(generic.ListView):
    template_name = templates['index']
    context_object_name = 'lastest_questions'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class DetailView(generic.DetailView):
    template_name = templates['detail']
    model = Question

class ResultsView(generic.DetailView):
    template_name = templates['results']
    model = Question

def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, templates['detail'], {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    