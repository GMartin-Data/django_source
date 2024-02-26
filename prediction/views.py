import json

from django.contrib.auth.decorators import login_required
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from django.shortcuts import render

from .forms import LoanApplicationForm


@login_required
def predict_api_page(request):
    url = "http://127.0.0.1:8000/predict"
    session = Session()

    # # TEMPLATE TO BE ADAPTED
    # # If this is a POST request we need to process the form data
    # if request.method == "POST":
    #     # Create a form instance and populate it with data from the request
    #     form = LoanApplicationForm(request.POST)
    #     # Check whether it's valid or not
    #     if form.is_valid():
    #         form.save()
    #         payload= json.dumps(form.cleaned_data)
    #         try:
    #             json_response = session.post(url, data=payload).json()
    #             print(json_response)
    #             return render(request, "prediction/predict.html",
    #                           context={"form": form, "data": json_response})
    #         except (ConnectionError, Timeout, TooManyRedirects, KeyError) as e:
    #             return render(request, "main/predict_api_page.html",
    #                         context={"form": form, "error": f"{type(e)}: {e}"})
    # else:
    #     form = LoanApplicationForm()
    # return render(request, "prediction/predict.html", context={"form": form})
