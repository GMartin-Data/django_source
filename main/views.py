from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# import pandas as pd
# import plotly.express as px 
# import plotly.offline as py


class SignupPage(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def sign_up(request):
    if request.method == 'POST':
        form = SignupPage(request.POST)
        if form.is_valid():
            form.save()
            # Redirection après une inscription réussie
            return redirect('success_page')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'sign_up.html', {'form': form})


def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def eda(request):

    # path_data = "main/cleandata.csv"
    # data = pd.read_csv(path_data)
    # data.State = data.State.dropna()
    # data.ApprovalYear = data.ApprovalYear.dropna()
    # data["SBA_Appv"] = data["SBA_Appv"].dropna()
    # data = data.groupby(['State', 'ApprovalYear'],).sum('SBA_Appv').sort_values(by='ApprovalYear', ascending=True).reset_index()
    # data = data[["State", "SBA_Appv", 'ApprovalYear']]
    # data = data.rename(columns={'SBA_Appv':'Amount guaranteed by SBA'})

    # fig = px.choropleth(data,
    #                     locations='State',
    #                     locationmode='USA-states',
    #                     scope="usa",
    #                     color='Amount guaranteed by SBA',
    #                     hover_name = 'State',
    #                     # hover_data = 'Amount guaranteed by SBA',
    #                     animation_frame='ApprovalYear',
    #                     color_continuous_scale='viridis',
    #                     title='AMOUNT OF LOANS GUARANTEED BY SBA TO EACH STATE OVER TIME')
    # # fig.update_geos(fitbounds="locations", visible=False)

    # fig.update_layout(width=800, height=600)
    # fig.show()

    # graph_interactif = py.plot(fig, filename='graphique_interactif.html')
    # Plotly.newPlot('graph-container', fig);
    # window.onload = loadGraph;
    return render(request, 'main/eda.html')


def model(request):
    return render(request, 'main/model.html')

@login_required
def special_page(request):
    return render(request, "main/special_page.html")

@login_required
def predict_page(request):
    return render(request, 'main/predict.html')

def graphique_interactif(request):
    return render(request, 'static/graphique_interactif.html')


from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect

def custom_logout(request):
    next_url = request.GET.get('next')  # Récupérer l'URL 'next' de la requête GET
    django_logout(request)
    if next_url:
        return redirect(next_url)  # Rediriger vers l'URL 'next' après la déconnexion
    else:
        # Rediriger vers la page actuelle si 'next' n'est pas spécifié
            return redirect(request.path)