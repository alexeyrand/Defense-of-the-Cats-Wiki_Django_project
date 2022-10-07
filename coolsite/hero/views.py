from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu_home = ["О сайте", "Форум", "Обратная связь"]
menu_home = [{'title': "О сайте", 'url_name': 'about'},
             {'title': "Форум", 'url_name': 'forum'},
             {'title': "Обратная связь", 'url_name': 'contact'},
             {'title': "Войти", 'url_name': 'login'}
]


def home(request):
    context = {
        'menu': menu_home,
        'title': 'Главная страница'
    }
    return render(request, 'home/home.html', context)


def about(request):
    return HttpResponse("<h1>О сайте</h1>")

def forum(request):
    return HttpResponse("<h1>Forum</h1>")

def contact(request):
    return HttpResponse("<h1>contact</h1>")

def login(request):
    return HttpResponse("<h1>О сайте</h1>")

def cats(request):
    post = Cat.objects.all()
    context = {
        'posts': post,
        'menu': menu_home,
        'title': 'Список котов'
    }
    return render(request, 'cats/cats.html', context)


def cat(request, catid):
    return render(request, 'cats/base_cat.html', {"menu": menu_home, "name": "base cat", 'title': f'Вики о коте {catid}'})


def enemy(request, enemyid):
    return render(request, 'enemies/red_rhino.html', {"menu": menu_home, "name": "red_rhino", 'title': f'Вики о враге {enemyid}'})


def enemies(request):
    return HttpResponse("<h1>Все враги</h1>")


def pageNotFound(request, exception):
    # return HttpResponseNotFound("<h1> 4 0 4 0 4 0 4</h1>")
    return redirect('home', permanent=True)
