from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accounts/dashboard.html')