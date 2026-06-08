from django.shortcuts import render

# Create your views here.
def info_view(request):
    return render(request, 'info.html')

def tovar_view(request):
    return render(request, 'tovar.html')

def cart_view(request):
    return render(request, 'cart.html')