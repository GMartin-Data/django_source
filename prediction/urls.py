from django.urls import path
from prediction import views


urlpatterns = [
    path('', views.predict_api_page, name='predict'),
]
