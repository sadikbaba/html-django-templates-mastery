from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render

def home(request):

    context = {
        'name': 'Sadik',
        'course': 'HTML + Django Templates'
    }
    return render(request, 'core/home.html', context)


def about(request):

     context = {
         'name': 'Sadik',
         'course': 'HTML + Django Templates'
     }
     return render(request, "core/about.html", context) 