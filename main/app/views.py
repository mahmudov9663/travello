from django.shortcuts import render
from .models import Destination
# Create your views here.

def home(request):

    dest1=Destination()
    dest1.img='destination_1.jpg.webp'
    dest1.name='London'
    dest1.price=700
    dest1.description='The most beautiiful city ever.'
    dest1.offer=True

    dest2=Destination()
    dest2.img='destination_2.jpg.webp'
    dest2.name='New York'
    dest2.price=679
    dest2.description='One of the most crowded city.'
    dest2.offer=False

    dest3=Destination()
    dest3.img='destination_3.jpg.webp'
    dest3.name='Tashkent'
    dest3.price=500
    dest3.description='Unknown City.'
    dest3.offer=False

    dests=[dest1, dest2, dest3]

    return render(request, 'home.html', {'dests': dests})

def calc(request):
    number1=int(request.POST['num1'])
    number2=int(request.POST['num2'])
    result=number1+number2
    return render(request, 'cal.html', {'result': result})