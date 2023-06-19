from django.urls import path
from django.views.generic import TemplateView
from chat import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name='index'),
    path("room/<str:slug>/", views.index, name="chat"),
    path("create/", views.create, name="create"),
    path("join/", views.join, name="join"),
]