from django.shortcuts import redirect, render

def home(request):
    return render(request, 'accounts/dashboard.html')