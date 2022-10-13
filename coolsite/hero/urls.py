from django.urls import path

from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("cats/", cats, name="cats"),
    path("enemies/", enemies, name="enemies"),
    path("cats/<slug:catname>", cat, name="cat"),
    path("enemies/enemy/<slug:enemyname>", enemy, name="enemy"),
    path("login/", login, name="login"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("forum/", forum, name="forum"),
    path("cats/<int:coll>/", coll, name="coll"),
    path('collections/', colls, name='colls')
]
