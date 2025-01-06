from django.shortcuts import render
from django.template.defaultfilters import title


def platform(request):
    title = 'главная страница'
    context = {
        'title' : title,
    }
    return render(request, 'third_task/platform.html', context)

def games(request):
    games = 'игры'
    context = {
        'games' : games,
    }
    return render(request,'third_task/games.html',context)

def cart(request):
    cors = 'корзина'
    context = {
        'cors' : cors,
    }
    return render(request, 'third_task/cart.html',context)

#
# Create your views here.


