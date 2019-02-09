from django.shortcuts import render, redirect
from django.http import HttpResponse
from chatbot.forms import QuestionForm, AnswerForm
# Create your views here.

def home(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return redirect('/chatbot')

    else:
        form = QuestionForm()
        args = {'form':form}
        return render(request,'chatbot/home.html',args)


def inference(request):
    return HttpResponse("Inference")
