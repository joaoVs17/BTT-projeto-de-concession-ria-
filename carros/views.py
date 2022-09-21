from multiprocessing import context
from pickletools import read_int4
from stat import FILE_ATTRIBUTE_SYSTEM
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import carros
from .models import Carro
from django.core.files.storage import FileSystemStorage
# Create your views here.

class Outros(View):
    def get(self,request):
        carrosSwiper = Carro.objects.all()[:3]
        carros = Carro.objects.all()
        context = {
            'carros': carros,
        }
        return render(request,'outros.html', context)
    def post(self,request):
        pass

class Add_Car(LoginRequiredMixin,View):
    login_url = 'login'
    redirect_field_name = '/carros/allProducts/'
    def get(self, request):
        if request.user.is_superuser == True:
            return render(request, 'add_Carro.html')
        else:
            return redirect('/carros/allProducts/?status=3')
    def post(self, request):
        placa = request.POST.get('placa')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')

        fs = FileSystemStorage(location='media/carPhotos/', base_url='/carPhotos/')
        upload = request.FILES['foto']
        print(upload.name)
        filename = fs.save(upload.name, upload)
        url = fs.url(filename)

        novoCarro = Carro(
            placa = placa,
            marca = marca,
            modelo = modelo,
            ano = ano,
            cor = cor,
            foto = url
        )
        novoCarro.save()
        return redirect('gerenciar')

@login_required(login_url='login')
def edit_car(request,pk):
    if request.user.is_superuser == True:
        carro = Carro.objects.get(pk=pk)
        if request.method == "GET":
            context = {
                'carro': carro,
            }
            return render(request, 'edit_Carro.html', context)
        elif request.method == "POST":
            placa = request.POST.get('placa')
            marca = request.POST.get('marca')
            modelo = request.POST.get('modelo')
            ano = request.POST.get('ano')
            cor = request.POST.get('cor')

            fs = FileSystemStorage(location='media/carPhotos/', base_url='/carPhotos/')
            upload = request.FILES['foto']
            print(upload.name)
            filename = fs.save(upload.name, upload)
            url = fs.url(filename)

            carro.placa = placa,
            carro.marca = marca,
            carro.modelo = modelo,
            carro.ano = ano,
            carro.cor = cor,
            carro.foto = url

            carro.save()
            return redirect('gerenciar')
    else:
        return redirect('/carros/allProducts/?status=3')

class Gerenciar(View):
    def get(self, request):
        status = request.GET.get('status')
        carros = Carro.objects.all().order_by('modelo')
        context = {
            'carros': carros,
            'status':status,
        }
        return render (request, 'gerenciar.html', context)
    def post(self, request):
        pass

@login_required(login_url='login')
def remove(request,pk):
    if request.user.is_superuser == True:
        carro = Carro.objects.get(pk=pk)
        carro.delete()
        return redirect('gerenciar')
    else:
        return redirect('/carros/allProducts/?status=3')

def car(request, pk):
    carro = Carro.objects.get(pk=pk)
    return render(request, 'carro.html', {'carro':carro})