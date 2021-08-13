from accounts.models import Account
from accounts.forms import RegistrationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    return 


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
            print('not valid form', reg_form)

    else:
        reg_form = RegistrationForm()

    context = {
        'reg_form': reg_form
    }

    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
def dashboard(request):
    return 