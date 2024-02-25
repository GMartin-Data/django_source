from django.views.generic import DetailView, ListView

from .models import Feature


class FeaturesListView(ListView):
    model = Feature
    template_name = "feats/feats_list.html"

class FeaturesDetailView(DetailView):
    model = Feature
    template_name = "feats/feats_detail.html"
