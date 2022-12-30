
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import (Http404, HttpRequest, HttpResponse,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django_omise.mixins import CheckoutMixin
from django_omise.models.choices import Currency

from .models import Bills, Food, Payment



# Your own class-based-view
class CheckoutView(LoginRequiredMixin, CheckoutMixin):

    template_name = "yourapp/template.html"
    # success_url = ...

    def get_charge_details(self):
        return {
            "amount": 100000,
            "currency": Currency.THB,
        }

    def process_charge_and_form(self, charge, form):
        if charge.status in [ChargeStatus.SUCCESSFUL, ChargeStatus.PENDING]:
            # Create new order and attach a charge object
            # And handle form data
            handle_form_data(form.cleaned_data)


def handler404(request, exception):
    return render(request, '404.html', status=404)