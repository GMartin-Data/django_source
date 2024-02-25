from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.SignupPage.as_view(), name="signup"),
    path("special/", views.special_page, name="special")
]
