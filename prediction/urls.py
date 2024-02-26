from django.urls import path
from prediction import views


urlpatterns = [
    path('', views.predict, name='predict'),
]
