from tests.models import Test
from django.contrib import messages
from client.models import Client
from django.shortcuts import redirect, render
from django.urls import path
from . import views
from .forms import ClientForm
from django.contrib.auth.decorators import login_required

import client

# Create your views here.
@login_required(login_url='login')
def new_client(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)

        if client_form.is_valid():
            print('form valid')
            user = request.user
            name = client_form.cleaned_data['name']
            email = client_form.cleaned_data['email']
            phone_number = client_form.cleaned_data['phone_number']
            state = client_form.cleaned_data['state']
            city = client_form.cleaned_data['city']

            # Check if already exists a client with the passed code
            code = client_form.cleaned_data['code']


            count = Client.objects.filter(code=code).count()
            print(count)
            
            #messages.error(request, 'Já possui um cliente com este CPF/CNPJ cadastrado')

            client = Client.objects.create(
                user=user,
                name=name,
                email=email,
                phone_number=phone_number,
                state=state,
                city=city,
                code=code
            )    

            client.save()

            messages.success(request, 'Cliente criado com sucesso')

            return redirect('new_client')
        
        else:
            return render(
                request, 
                'client/new-client.html', 
                context={'client_form': client_form}
            )
            

    client_form = ClientForm()
    context = {
        'client_form': client_form
    }
    return render(request, 'client/new-client.html', context)
    
    
def client_detail(request, client_id):
    client_profile = Client.objects.get(id=client_id)
    tests = Test.objects.filter(client_id=client_id)

    context = {
        'client': client_profile,
        'tests': tests
    }

    return render(request, 'client/client-detail.html', context)


@login_required(login_url='login')
def clients(request):
    clients = Client.objects.all()
    clients_count = clients.count()

    context = {
        'page_name': 'Clientes',
        'clients': clients,
        'clients_count': clients_count
    }

    return render(request, 'client/clients-table.html', context)


@login_required(login_url='login')
def my_clients(request):
    clients = Client.objects.filter(user_id=request.user.id)
    clients_count = clients.count()

    context = {
        'page_name': 'Meus Clientes',
        'clients': clients,
        'clients_count': clients_count
    }

    return render(request, 'client/clients-table.html', context)