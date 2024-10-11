from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Tag
from main.myforms import ContactForm

def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})

def contact_view(request):
    if request.method == 'POST':
        print("hola")
        form = ContactForm(request.POST)
        if form.is_valid():
            print("entro")
            form.save()
            return redirect('success_page')
    else:
        print("No entro")
        form = ContactForm()
        print("entro aqui")
    return render(request, 'contact.html', {'form': form})      

def success_page_view(request):
    return render(request, 'success_page.html')  




