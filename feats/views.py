from django.views.generic import ListView

from .models import Feature


class FeaturesListView(ListView):
    model = Feature
    template_name = "feats/feats_list.html"
