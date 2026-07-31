from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    context = {
        'name': 'Sadik',
        'projects': projects
    }
    return render(request, 'core/home.html', context)

def about(request):

     context = {
         'name': 'Sadik',
         'course': 'HTML + Django Templates'
     }
     return render(request, "core/about.html", context) 


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # or a success page
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})