from django.contrib import auth
from accounts.models import Account
from accounts.forms import RegistrationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from client.models import Client
from tests.models import Test

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:

            # Get user params
            auth.login(request, user)

            return redirect('dashboard')

        else:
            messages.error(request, 'Email ou senha incorretos')
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect ('login') 


def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)

        if reg_form.is_valid():
            print('valid form')
            first_name = reg_form.cleaned_data['first_name']
            last_name = reg_form.cleaned_data['last_name']
            email = reg_form.cleaned_data['email']
            username = email.split("@")[0]
            password = reg_form.cleaned_data['password']
            
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )

            user.save()

            messages.success(request, "Perfil criado com sucesso")
            return redirect('login')

    else:
        reg_form = RegistrationForm()

    context = {
        'reg_form': reg_form
    }

    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def dashboard(request):
    clients = None
    clients_count = 0

    if request.user.is_authenticated:
        user = request.user
        clients = Client.objects.filter(user_id=user.id)

        if len(clients) != 0:
            clients_count = clients.count()
        else:
            clients_count = 0

        tests = Test.objects.filter(user_id=user.id)
        finished_tests = Test.objects.filter(status='Finalizado', user_id=user.id)
        tests_count = finished_tests.count()

        unfinished_tests = tests.filter(status='Em andamento')
        unfinished_tests_count = unfinished_tests.count()

        latest_tests = tests.order_by('-created_at')

        if len(latest_tests) > 5:
            latest_tests = latest_tests[:5]
        
        top_clients = clients.order_by('-grade')

        if len(top_clients) > 5:
            top_clients = top_clients[:5]

        
    
    context = {
        'clients': top_clients,
        'clients_count': clients_count,
        'tests': latest_tests,
        'tests_count': tests_count,
        'unfinished_tests_count': unfinished_tests_count
    }

    return render(request, 'accounts/dashboard.html', context)