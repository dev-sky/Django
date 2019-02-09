from django.db import models
from django.db.models.signals import post_save


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 100)
    question_id = models.IntegerField(primary_key = True)
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    answer_text = models.CharField(max_length = 100)
    answer_id = models.OneToOneField(Question,on_delete = models.CASCADE,primary_key = True)

    def __str__(self):
        return self.answer_text

def creating_answer_function(sender,**kwargs):
    if kwargs['created']:
       answer = "hi"
       print("hi")
       obj = Answer.objects.create(answer_id = kwargs['instance'].question_id, answer_text = answer)
       obj.save()
post_save.connect(creating_answer_function,sender = Question)
