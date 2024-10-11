from django.urls import path
from . import views
from .myforms import ContactForm

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    #path("contact/", views.contact, name="contact"),
    path("contact/", views.contact_view, name="contact"),
    path("project/<int:id>/", views.project, name="project"),
    path('succes_page/', views.success_page_view, name='success_page')
]