from django import template
from hero.models import *


register = template.Library()

@register.simple_tag()
def get_collections():
    return Collection.objects.all()


@register.inclusion_tag('tags/top_menu_home.html', takes_context=True)
def show_top_menu_home(context):
    top_menu = [{'title': "О сайте", 'url_name': 'about'},
                 {'title': "Форум", 'url_name': 'forum'},
                 {'title': "Добавить кота", 'url_name': 'addpost'},
                 {'title': "Обратная связь", 'url_name': 'contact'},
                 {'title': "Войти", 'url_name': 'login'}
                ]
    return {'top_menu': top_menu, "context": context}

@register.inclusion_tag('tags/left_menu_home.html')
def show_left_menu_home():
    left_menu = [{'title': "Главная", 'url_name': 'home', 'selected': 'home'},
                 {'title': "Все коты", 'url_name': 'cats', 'selected': 'cats'},
                 {'title': "Все враги", 'url_name': 'enemies', 'selected': 'enemies'},
                 {'title': "Все коллекции", 'url_name': 'colls', 'selected': 'colls'},
                 {'title': "Все уровни", 'url_name': 'colls', 'selected': 'colls'},
                ]
    return {'left_menu': left_menu}
