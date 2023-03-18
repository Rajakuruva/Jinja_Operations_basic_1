from django.shortcuts import render

# Create your views here.

def Keypad(request):
    return render(request,"Keypad.html")

def Computer(request):
    return render(request,'Computer.html')