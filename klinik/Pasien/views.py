from django.shortcuts import render

from .models import Data_Pasien

def index(request):
    hasil=Data_Pasien.objects.all()
    print(hasil)
# Create your views he