from django.urls import path

from .views import *

urlpatterns = [
    path("", HeroHome.as_view(), name="home"),
    path("cats/<slug:showcats>", Cats.as_view(), name="cats"),
    path("enemies/", enemies, name="enemies"),
    path("cats/post/<slug:catname>", Cat_post.as_view(), name="cat"),
    path("enemies/enemy/<slug:enemyname>", enemy, name="enemy"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("forum/", forum, name="forum"),
    path("addpost/", addpost, name="addpost"),
    path("addcat/", AddCat.as_view(), name="addcat"),
    path('collections/', Collections.as_view(), name='colls'),
    path('collections/<slug:collname>', Collection_post.as_view(), name='coll'),
]
