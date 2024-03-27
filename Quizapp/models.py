
from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    

class Choice(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)  # optional field
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    is_selected = models.BooleanField()

