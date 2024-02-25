from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from .models import Feature


# Note: LoginRequiredMixin has to be on the left
# In order to be the first class to inherit from
class FeaturesListView(LoginRequiredMixin, ListView):
    model = Feature
    template_name = "feats/feats_list.html"

class FeaturesDetailView(DetailView):
    model = Feature
    template_name = "feats/feats_detail.html"
