from django.shortcuts import render
from django.views import View
# Create your views here.
class Outros(View):
    def get(self,request):
        return render(request, 'outros.html')
    def post(self, request):
        pass

class Add_Car(View):
    def get(self, request):
        return render(request, 'add_Carro.html')
    def post(self, request):
        pass