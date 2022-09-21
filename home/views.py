from django.shortcuts import render
from django.views import View
from carros.models import Carro
import random
# Create your views here.

class Home(View):
    def get(self,request):
        status = request.GET.get('status')
        carros = Carro.objects.all()
        randomIndex = random.randrange(len(carros))
        randomCar = carros[randomIndex]
        car = carros.exclude(placa=randomCar.placa)
        randomIndex = random.randrange(len(car))
        randomCar1 = car[randomIndex]
        car = car.exclude(placa=randomCar1.placa)
        print(car)
        randomIndex = random.randrange(len(car))
        randomCar2 = car[randomIndex]
        context = {
            'carros': carros,
            'randomCar': randomCar,
            'randomCar1': randomCar1,
            'randomCar2': randomCar2,
            'status': status,
        }
        return render(request, 'home.html', context)
    def post(self, request):
        pass