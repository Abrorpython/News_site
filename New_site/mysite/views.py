from django.shortcuts import render
from .models import *


def index(request):
    als = News.objects.all().order_by('-created_time')
    a = News.objects.all().order_by('-created_time')[:3]
    tex = Category.objects.get(id=8)
    x = News.objects.all().filter(category_id=1)
    politika = News.objects.all().filter(category_id=2)
    obshestva = News.objects.all().filter(category_id=3)
    sport = News.objects.all().filter(category_id=5)
    y = News.objects.all().filter(category_id=6)
    nno = News.objects.all().filter(category_id=7)
    texnologiya = News.objects.all().filter(category_id=8)
    alls = News.objects.all().order_by('-created_time')[10:12]
    ctx = {
        "a": a[0],
        "b": a,
        "als": als,
        "tex": tex,
        "texno": texnologiya,
        "x": x,
        "y": y,
        "sport": sport,
        "obsh": obshestva,
        "alls": alls,
        "poli": politika,
        "nno": nno,
    }
    return render(request, "index.html", ctx)


def category(request, n):
    c = Category.objects.get(id=n)
    yangiliklar = News.objects.all().filter(category_id=n)
    new = News.objects.all().filter(category_id=n).order_by('-created_time')
    ctx = {
        "s": c,
        "name": yangiliklar,
        "new": new[0],
    }

    return render(request, "category.html", ctx)


def contact(request):
    return render(request, "contact.html", {})


def search(request):
    return render(request, "search.html", {})


def view(request, pk):
    a = News.objects.all().get(id=pk)
    b = News.objects.all().filter(category_id=pk)
    ctx = {
        "a": a,
        "b": b,
    }
    return render(request, "view.html", ctx)
