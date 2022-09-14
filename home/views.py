from django.shortcuts import render
from django.views import View
# Create your views here.

class Home(View):
    def get(self,request):
        status = request.GET.get('status')
        context = {
            'status': status,
        }
        return render(request,'home.html', context)
    def post(self,request):
        pass