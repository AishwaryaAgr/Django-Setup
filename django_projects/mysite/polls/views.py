from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 7884205c is the polls index.")