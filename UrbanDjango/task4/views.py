from django.shortcuts import render
from django.template.defaultfilters import title
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    return render(request, 'platform.html')


def game(request):
    title_g = "Игры"
    games = {"Atomic Heart", "Cyberpunk 2077", "PayDay 2"}
    context = {
        'title_g': title_g,
        'games': games
    }
    return render(request, 'games.html', context)


def cart(request):
    title_p = "Корзина"
    content_p = "Это всё иллюзия и ничего не купите (:"
    context = {
        "title_p": title_p,
        "content_p": content_p
    }
    return render(request, 'cart.html', context)


def menu(request):
    title = "Главная страница"
    main = "Главная"
    game = "Магазин"
    cart = "Корзина"
    context = {
        'title': title,
        'main': main,
        'game': game,
        'cart': cart,
    }
    return render(request, "menu.html", context)
