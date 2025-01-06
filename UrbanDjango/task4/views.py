from django.shortcuts import render
from django.template.defaultfilters import title


def platform(request):
    title = 'главная страница'
    context = {
        'title' : title,
    }
    return render(request, 'fourth_task/platform.html', context)

def games(request):
    games = ["Atomic Heard", "Cyberpunk 2077", "PayDay 2"]
    context = {
        'games' : games,
    }
    return render(request,'fourth_task/games.html',context)

def cart(request):
    cors = 'корзина'
    context = {
        'cors' : cors,
    }
    return render(request, 'fourth_task/cart.html',context)

def base(request):
    return render(request, 'fourth_task/menu.html')

#
# Create your views here.


