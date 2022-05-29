from django.shortcuts import render

from django.views.generic import View

class EmployerHomeView(View):
    def get(self,request):
        return render(request,"emp-home.html")
