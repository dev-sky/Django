from django.db import models

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
