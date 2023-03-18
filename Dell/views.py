from django.shortcuts import render

# Create your views here.
def Laptop(request):
    return render(request,'Laptop.html')

def Phone(request):
    return render(request,'Phone.html')