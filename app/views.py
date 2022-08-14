from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'register.html')


def event(request):
    return render(request, 'event.html')


def news(request):
    return render(request, 'news.html')


def announcements(request):
    return render(request, 'announcements.html')


def publications(request):
    return render(request, 'publications.html')


def contact(request):
    return render(request, 'contact.html')
