from django.shortcuts import render,redirect
from .models import Question,Choice,Quiz
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import HttpResponse

@login_required(login_url="login")
def home(request):
    profile = Profile.objects.get(user=request.user)
    if profile.played_before:
        return HttpResponse("You have already played the game.")
    else:
        questions = Question.objects.all()
        score = 0
        if request.method == 'POST':
            total_questions = Question.objects.count()
            for question in questions:
                selected_choice_id = request.POST.get(f'question{question.id}')
                if selected_choice_id is not None:
                    correct_choice = Choice.objects.get(question=question, is_correct=True)
                    if int(selected_choice_id) == correct_choice.id:
                        score += 1
                        print(score)
                        profile.score = score
                        profile.played_before= True
                        profile.save()

    return render(request, 'home.html', {'questions': questions,'score':score})

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        User.objects.create_user(username=username,
                                 password=password,
                                 email=email,
        )
        return redirect('login')
    return render(request, 'register.html')    
    
def loginn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user =authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request, 'login.html')

def logoutt(request):
    logout(request)
    return redirect('home')