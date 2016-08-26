from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def senddata(request):
    data = request.GET.get("data", "")
    logger.info(data)
    return HttpResponse(data + "ok")