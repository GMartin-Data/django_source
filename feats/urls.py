from django.urls import path

from . import views


urlpatterns = [
    path('', views.FeaturesListView.as_view(), name='feat_list')
]
