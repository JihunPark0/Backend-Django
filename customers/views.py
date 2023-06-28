from customers.models import Customer
from django.http import JsonResponse
from django.http import Http404
from customers.serialisers import CustomerSerieliser
def customers(request):
    #invoke serialiser which turns database object to json
    data = Customer.objects.all()
    serialiser = CustomerSerieliser(data, many=True)
    return JsonResponse({'customers':serialiser.data})
def customer(request,id):
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        raise Http404("Customer doesn't exist")
    serialiser = CustomerSerieliser(data)
    return JsonResponse({'customer':serialiser.data})