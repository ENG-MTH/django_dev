from django.http import HttpResponse
from django.shortcuts import render


def index(requset):
    conditon = True
    list_of_names = ['Hajas', 'marwa', 'sofymz']

    return render(requset, 'enclopedia/list.html.html', context={

        'conditon': conditon,
        'list_of_names': list_of_names,

    })



def say_hi(request, name: str):
    captialized_name = name.capitalize()
    conditon = True
    list_of_names = ['Hajas', 'marwa', 'sofymz']

    return render(request, 'enclopedia/index.html', context={
        'name': name.capitalize(),
        'conditon': conditon,
        'list_of_names': list_of_names,

    })
