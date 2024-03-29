
from django.db import models
from django.contrib.auth.models  import User

class Quiz(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE,blank=True,null=True)
    text = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE,blank=True,null=True)
    text = models.CharField(max_length=255,blank=True,null=True)  # blank for optional choices
    is_correct = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.text
    
    
    
class Profile(models.Model):
    score=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    
                                