from django.shortcuts import render

# Create your views here.

def reset_password(request):
    return render(request, 'passapp/reset_password.html')