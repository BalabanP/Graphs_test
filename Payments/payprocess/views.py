from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponseServerError
from payprocess.main import main_module

@api_view(['POST'])
def ProcesPayment(request):
    try:
        if request.method == 'POST':
            data = request.POST
            if main_module(data):
                return Response("Payment is procesed")
            else:
                return Response("The request is invalid",status= status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponseServerError()
