from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question, Choice, Data6369
from django.template import loader
from django.urls import reverse
from django.views import generic
from io import TextIOWrapper,StringIO
import csv

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question

class ResultsView(generic.DetailView):
    model = Question
    template_name =  "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def upload(request):
    # リクエストファイルに'csv'が入っていれば
    if 'csv' in request.FILES:
        from_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        # csv.reader(csvfile)⇢csvファイルを行ごとに読み込むときに必要？
        csv_file = csv.reader(from_data)
        for line in csv_file:
            data6369, created = Data6369.objects.get_or_create(start_week=line[2])
            data6369.index = line[0]
            data6369.start_week = line[1]
            data6369.end_week = line[2]
            data6369.start_price = line[3]
            data6369.last_price = line[4]
            data6369.high_price =line[5]
            data6369.low_price = line[6]
            data6369.rsi = line[7]
            data6369.moveaverage = line[8]
            data6369.stdev = line[9]
            data6369.bb = line[10]
            data6369.save()
        return render(request, 'polls/upload.html')
    
    else:
        return render(request, 'polls/upload.html')