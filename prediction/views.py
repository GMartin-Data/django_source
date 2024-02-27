import json

from django.contrib.auth.decorators import login_required
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django.shortcuts import render
import datetime
from .forms import LoanApplicationForm


@login_required
def predict_api_page(request):
    url = "http://127.0.0.1:8000/predict"
    session = Session()

    # TEMPLATE TO BE ADAPTED
    # If this is a POST request we need to process the form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = LoanApplicationForm(request.POST)
        # Check whether it's valid or not
        if form.is_valid():
            form.save()
            payload= json.dumps(form.cleaned_data)
            print(form.cleaned_data)
            
            regions = {
                "AL": "Southeast",
                "AK": "Northwest",
                "AZ": "Southwest",
                "AR": "Southeast",
                "CA": "Southwest",
                "CO": "Southwest",
                "CT": "Northeast",
                "DE": "Northeast",
                "FL": "Southeast",
                "GA": "Southeast",
                "HI": "Northwest",
                "ID": "Northwest",
                "IL": "Northeast",
                "IN": "Northeast",
                "IA": "Northwest",
                "KS": "Northwest",
                "KY": "Southeast",
                "LA": "Southeast",
                "ME": "Northeast",
                "MD": "Northeast",
                "MA": "Northeast",
                "MI": "Northeast",
                "MN": "Northwest",
                "MS": "Southeast",
                "MO": "Northwest",
                "MT": "Northwest",
                "NE": "Northwest",
                "NV": "Northwest",
                "NH": "Northeast",
                "NJ": "Northeast",
                "NM": "Southwest",
                "NY": "Northeast",
                "NC": "Southeast",
                "ND": "Northwest",
                "OH": "Northeast",
                "OK": "Southwest",
                "OR": "Northwest",
                "PA": "Northeast",
                "RI": "Northeast",
                "SC": "Southeast",
                "SD": "Northwest",
                "TN": "Southeast",
                "TX": "Southwest",
                "UT": "Northwest",
                "VT": "Northeast",
                "VA": "Southeast",
                "WA": "Northwest",
                "WV": "Southeast",
                "WI": "Northwest",
                "WY": "Northwest", 
                'DC' : 'Northeast'
            }

            recession_periods = [
                (1969, 1970),
                (1973, 1975),
                (1980, 1980),
                (1981, 1982),
                (1990, 1991),
                (2001, 2001),
                (2007, 2009),
                (2020, 2020),  # Including the COVID-19 pandemic recession
            ]

            # Function to check if a given year (from dt.year) was in recession
            def is_year_in_recession(year):
                # The year parameter is expected to be an integer
                return any(start <= year <= end for start, end in recession_periods)
        

            formulaire = form.cleaned_data
            print(regions[formulaire["state"]])
            print(True) if formulaire["state"] == formulaire["bank_state"] else print(False)

            date = datetime.datetime.now()

            new_info = {
                "Region" : regions[formulaire["state"]],
                "SameState" : True if formulaire["state"] == formulaire["bank_state"] else False,
                "Year": date.year,
                "Month" : date.month,
                "Day" : date.day,
                "DayOfWeek" : date.weekday(),
                "Recession" : is_year_in_recession(date.year)
                }
            formulaire.update(new_info)
            formulaire = {key.title(): value for key, value in formulaire.items()}
            print(formulaire)
            
            try:
                json_response = session.post(url, data=formulaire).json()
                print(json_response)
                return render(request, "prediction/predict.html",
                              context={"form": form, "data": json_response})
            except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
                return render(request, "main/predict_api_page.html",
                            context={"form": form, "error": f"{type(e)}: {e}"})
    else:
        form = LoanApplicationForm()
    return render(request, "prediction/predict.html", context={"form": form})