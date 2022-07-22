"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpRequest, HttpResponse
import random

politic = {
    1: {"name": "prime minister", "fullname": "Boris Johnson", "id": 1},
    2: {"name": "european commission", "fullname": "Ursula von der Leyen", "id": 2},
    3: {"name": "potato", "fullname": "Alexander Lukashenko", "id": 3},
    4: {"name": "president", "fullname": "Volodimir Zelenskiy", "id": 4}
}


def first_page(request):
    return HttpResponse('Tiurin Home Work')


def page_view(request: HttpRequest, article_id, article_slug):
    return HttpResponse(f"{article_id} {article_slug}")


def politic_list(request):
    return HttpResponse(politic.values())


def pass_word(request, password):
    good_password = "".join(x for x in password if x.isalnum())
    if len(password) == 8:
        if good_password == password:
            return HttpResponse("Good password")
        else:
            return HttpResponse("No, no, no, no this password is bad")
    else:
        return HttpResponse("No, no, no, no this password is bad")


def random_pass(request, length):
    password = ''
    for x in range(int(length)):
        password += random.choice(list("1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"))
    return HttpResponse(f"OK, take your password:  {password}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page),
    path('home', first_page),
    path('homepage', first_page),
    path('article/<int:article_id>/<str:article_slug>', page_view),
    path('politic', politic_list),
    path('password/<password>', pass_word),
    path('password/generate/<length>', random_pass)
]
