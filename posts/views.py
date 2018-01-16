from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def index(request):
    return render_to_response(request,'posts/index.html')