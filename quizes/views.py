from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
# Create your views here.

class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/main.html'


