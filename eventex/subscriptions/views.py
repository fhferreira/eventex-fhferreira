from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    """Callable recebendo http request e retorna http response"""
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

