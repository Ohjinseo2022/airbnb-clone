from django.urls import URLPattern


from django.urls import path
from . import views

urlpatterns = [
    path("", views.say_hello),
]
