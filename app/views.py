from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def apply(request):
    return render(request, 'apply.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    return render(request, 'register.html')


def staff(request):
    return render(request, 'staff.html')


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


def cohort(request, id):
    match id:
        case '1':
            return render(request, 'cohort_one.html')
        case '2':
            return render(request, 'cohort_two.html')
        case '3':
            return render(request, 'cohort_three.html')
        case '4':
            return render(request, 'cohort_four.html')
        case '5':
            return render(request, 'cohort_five.html')
