from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context = {'title': 'Home',
               'content': 'Главная страница магазина - HOME',
               'list': ['first', 'second', 'third'],
               'dict': {'first': 1, 'second': 2, 'third': 3},
               'is_authenticated': True
               }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About page")

# Create your views here.
