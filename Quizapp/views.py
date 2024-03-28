from django.shortcuts import render,redirect
from .models import Question,Choice,Quiz
from django.contrib import messages


def home(request):
    questions = Question.objects.all()
    score = 0
    if request.method == 'POST':
         selected_choice_id = None
         total_questions = Question.objects.count()
            
    for question in questions:
        selected_choice_id = request.POST.get(f'question{question.id}')
        if selected_choice_id is not None:
            print(selected_choice_id)
            correct_choice = Choice.objects.get(question=question, is_correct=True)
            if int(selected_choice_id) == correct_choice.id:
                score += 1
                print(score)

    return render(request, 'home.html', {'questions': questions,'score':score})