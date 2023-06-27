from customers.models import Customer
from django.http import JsonResponse
from customers.serialisers import CustomerSerieliser
def customers(request):
    #invoke serialiser which turns database object to json
    data = Customer.objects.all()
    serialiser = CustomerSerieliser(data, many=True)
    return JsonResponse({'customers':serialiser.data})