from django.urls import path, include
from . import views
from project import *


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("signup/", views.SignupPage.as_view(), name="signup"),
    path("special/", views.special_page, name="special"),
    path('predict/', include('prediction.urls'), name="pred"),
    path('eda/', views.eda, name="eda"),
    path('model/', views.model, name="model"),
    path('predict/', views.predict_page, name="predict"),
    path('', views.graphique_interactif, name="graphique_interactif"),
    path('', views.custom_logout, name="custom_logout")
]
