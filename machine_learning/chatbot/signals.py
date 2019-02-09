from chatbot.forms import AnswerForm
from chatbot.models import Question, Answer
from django.shortcuts import redirect
#function calling the inference script
def inference(input_model):
    returns "This is the answer bitch!"


def creating_answer_function(sender,**kwargs):
    if **kwargs['created']:
        answer = inference(**kwargs['instance'].question_text)
        obj = Answer.objects.create(answer_id = **kwargs['instance'].question_id, answer_text = answer)
        return redirect('/chatbot/inference')
