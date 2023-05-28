from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return HttpResponse('<h1> msd is a great captain</h1>')
def raina(request):
    return HttpResponse('<h2> raina is MR ipl</h2>')