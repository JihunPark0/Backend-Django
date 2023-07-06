from customers.models import Customer
from django.http import JsonResponse
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from customers.serialisers import CustomerSerieliser
@api_view(['GET', 'POST'])
def customers(request):
    #invoke serialiser which turns database object to json
    if request.method =='GET':

        data = Customer.objects.all()
        serialiser = CustomerSerieliser(data, many=True)
        return Response({'customers':serialiser.data})
    elif request.method == 'POST':
        serialiser = CustomerSerieliser(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'customer': serialiser.data}, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.Http_400_BAD_REQUEST)
@api_view(['GET', 'POST', 'DELETE']) #decorators
def customer(request,id):
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        #raise Exception()
        serialiser = CustomerSerieliser(data)
        return Response({'customer':serialiser.data})
    elif request.method =='DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method =='POST':
        serialiser = CustomerSerieliser(data, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'customer': serialiser.data})
        return Response(serialiser.errors, status=status.Http_400_BAD_REQUEST)