from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Data


@api_view(['GET'])
def getUuid(request):
    instance = Data.objects.create()
    instance.save()

    data = Data.objects.order_by('-time_stamp')
    response = {}
    for item in data:
        response[str(item.time_stamp)] = item.id
    return Response(response, status=200)
