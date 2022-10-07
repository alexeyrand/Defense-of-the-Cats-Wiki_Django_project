from django.urls import path

from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("cats/", cats, name="cats"),
    path("enemies/", enemies, name="enemies"),
    path("cats/cat/<int:catid>", cat, name="cat"),
    path("enemies/enemy/<int:enemyid>", enemy, name="enemy"),
    path("login/", login, name="login"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("forum/", forum, name="forum"),
]
