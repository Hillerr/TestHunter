from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Test, TestImages 
from client.models import Client
from django.contrib import messages
import datetime
from .utils import *
from .forms import TestForm, TestImageForm

# Create your views here.
@login_required(login_url='login')
def new_test(request):
    if request.method == 'POST':
        try:
            test = Test()
            save_test(request, test)
        except Exception as ex:
            messages.error(request, ex)
            return redirect('new_test')

        messages.success(request, 'Teste cadastrado com sucesso')
        return redirect('new_test')
    
    x = 1 

    test_choices = TestForm()
    context = {
        'form': test_choices
    }

    return render(request, 'tests/new-test.html', context)


@login_required(login_url='login')
def tests(request):
    tests = Test.objects.all().order_by('-created_at')
    context = {
        'tests': tests,
        'page_name': 'Testes'
    }
    return render(request, 'tests/tests-table.html', context)


@login_required(login_url='login')
def my_tests(request):
    tests = Test.objects.filter(user_id=request.user.id).order_by('-created_at')
    context = {
        'tests': tests,
        'page_name': 'Meus Testes'
    }
    return render(request, 'tests/tests-table.html', context)


@login_required(login_url='login')
def my_unfinished_tests(request):
    tests = Test.objects.filter(user_id=request.user.id, status='Em andamento').order_by('-created_at')
    context = {
        'tests': tests,
        'page_name': 'Meus testes em andamento'
    }
    return render(request, 'tests/tests-table.html', context)


@login_required(login_url='login')
def test_detail(request, test_id):
    test = Test.objects.get(id=test_id)
    tests = Test.objects.filter(product_tested=test.product_tested).exclude(id=test.id)
    
    if request.user == test.user:
        creator = True
    else:
        creator = False

    test_images = TestImages.objects.filter(test_id=test_id)
    test_images_count = test_images.count()

    context = {
        'test': test,
        'tests': tests,
        'creator': creator,
        'test_images': test_images,
        'test_images_count': test_images_count
    }

    return render(request, 'tests/test-detail.html', context)


@login_required(login_url='login')
def edit_test(request, test_id):
    try:
        test = Test.objects.get(id=test_id, user_id=request.user.id)
    except Test.DoesNotExist:
        messages.error('Somente o usu??rio que cadastrou o teste pode edit??-lo')
        return redirect('edit_test')

    if request.method == 'POST':
        try:
            save_test(request, test)
        except Exception as ex:
            messages.error(request, ex)

        messages.success(request, 'Teste editado com sucesso')

        return redirect('test_detail', test_id)

    form = TestForm(initial={'test_type': test.test_type})
    images = TestImages.objects.filter(test_id=test_id)

    context = {
        'form': form, 
        'test': test,
        'image_form': TestImageForm(),
        'images': images
    }

    return render(request,'tests/test-edit.html', context)


@login_required(login_url='login')
def finish_test(request):
    if request.method == 'POST':
        test_id = request.POST['test_id']

        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            messages.error(request, f"Teste com id {test_id} n??o foi encontrado")
            return redirect('test_detail', test_id)

        for field in vars(test):
            if test.__dict__[field] == '' or test.__dict__[field] is None:
                messages.error(request, "Todos os campos do formul??rio devem ser preenchidos")
                return redirect('test_detail', test_id)
        
        test.status = 'Finalizado'
        test.save()
        messages.success(request, f"Teste do produto {test.product_tested} finalizado com sucesso")

    return redirect('my_tests')


@login_required(login_url='login')
def remove_test(request):
    if request.method == 'POST':
        test_id = request.POST['test_id']

        try:
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            messages.error(request, f"Teste com id {test_id} n??o foi encontrado")
            return redirect('test_detail', test_id)

        test.delete()
        messages.success(request, f"Teste do produto {test.product_tested} removido com sucesso")

    return redirect('my_tests')


@login_required(login_url='login')
def add_test_image(request, test_id):
    if request.method == 'POST':
        form = TestImageForm(request.POST, request.FILES)

        if form.is_valid():
            test_image = TestImages()
            test_image.test = Test.objects.get(id=test_id)
            test_image.image = request.FILES['image']
            test_image.save()

    return redirect('edit_test', test_id)


@login_required(login_url='login')
def remove_test_image(request, test_id, image_id):
    image = TestImages.objects.get(id=image_id)
    image.delete()
    return redirect('edit_test', test_id)



        



