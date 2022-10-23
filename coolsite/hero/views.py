from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic.detail import BaseDetailView
from django.urls import reverse_lazy

class HeroHome(TemplateView):
#    model = Collection
    template_name = 'home/home.html'


class Collections(ListView):
    paginate_by = 5
    model = Collection
    template_name = 'collections/collections.html'
    context_object_name = 'colls'
    allow_empty = False                                                          #вызывает 404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все коллекции'
        return context


class Collection_post(DetailView):
    model = Collection
    template_name = 'collections/collection.html'
    context_object_name = 'coll'
    slug_url_kwarg = 'collname'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['coll']
        catscoll = Collection.objects.get(slug = self.kwargs['collname']).get_cats.all()
        context['cats'] = catscoll
        return context


class Cats(ListView):
    paginate_by = 5
    showname = 'all_cats'
    model = Cat
    template_name = 'cats/cats.html'
    context_object_name = 'cats'
    allow_empty = False                                                          #вызывает 404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все коты'
        context['colls'] = Collection.objects.all()
        return context

    def get_queryset(self):
        if self.kwargs['showcats'] == 'all_cats':
            return Cat.objects.filter(is_published=True)
        else:
            return Cat.objects.filter(coll__slug=self.kwargs['showcats'],   is_published=True)


class Cat_post(DetailView):
    model = Cat
    template_name = 'cats/cat.html'
    context_object_name = 'cat'
    slug_url_kwarg = 'catname'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['cat']
        return context


class AddCat(CreateView):
    form_class = AddCatForm
    template_name = 'addpost/addcat.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить кота'
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "user/register.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    return HttpResponse("<h1>О сайте</h1>")

def forum(request):
    return HttpResponse("<h1>Forum</h1>")

def contact(request):
    return HttpResponse("<h1>contact</h1>")



def addpost(request):
    context = {
        'title': 'Добавить пост',
    }
    return render(request, 'addpost/addpost.html', context)

def addcat(request):
    if request.method == 'POST':
        form = AddCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddCatForm()

    context = {
        'form': form,
        'title': 'Добавить кота',
    }
    return render(request, 'addpost/addcat.html', context)




def enemy(request, enemyid):
    return render(request, 'enemies/red_rhino.html', {"menu": menu_home, "name": "red_rhino", 'title': f'Вики о враге {enemyid}'})


def enemies(request):
    return HttpResponse("<h1>Все враги</h1>")


def pageNotFound(request, exception):
    # return HttpResponseNotFound("<h1> 4 0 4 0 4 0 4</h1>")
    return redirect('home', permanent=True)























#######################


#def home(request):
#    context = {
#        'title': 'Главная страница',
#        'cat_selected': 0,
#    }
#    return render(request, 'home/home.html', context)


#def colls(request,):

#    coll = Collection.objects.all()
#    context = {
#        'title': 'Список коллекций',
#        'colls': coll,
#        'cat_selected': 'colls',
#    }
#    return render(request, 'collections/collections.html', context)

#def coll(request, collname):
#    post = get_object_or_404(Collection, slug = collname)
#    colle = Collection.objects.filter(slug = collname)
#    cats = Cat.objects.filter(coll = colle[0].id)
#    print(cats)
#    context = {
#        'post': post,
#        'cats': cats,
#        'title': post.name,
#    }
#    return render(request, 'collections/collection.html', context)

#def cats(request, showcats):
#    if showcats == 'all_cats':
#        post = Cat.objects.all()
#    else:
#        colle = Collection.objects.filter(slug = showcats)
#        post = Cat.objects.filter(coll = colle[0].id)
#    coll = Collection.objects.all()
#    context = {
#        'posts': post,
#        'title': 'Список котов',
#        'colls': coll,
#        'cat_selected': 'cats',
#    }
#    return render(request, 'cats/cats.html', context)



#def cat(request, catname):
#    cat = get_object_or_404(Cat, slug = catname)
#
#    context = {
#        'cat': cat,
#        'title': cat.name
#    }
#    return render(request, 'cats/cat.html', context)
