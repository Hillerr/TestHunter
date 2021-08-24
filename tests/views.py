from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Test 
from client.models import Client
from django.contrib import messages
import datetime

# Create your views here.
@login_required(login_url='login')
def new_test(request):
    if request.method == 'POST':
        test = Test()
        test.user = request.user
        test.product_tested = request.POST['product_tested']
        client_code = request.POST['client_code']

        try: 
            client = Client.objects.get(code=client_code)
        except Client.DoesNotExist:
            messages.error(request, f"Não foi encontrado nenhum cliente com o CPF/CNPJ {client_code}. Por favor, cadastre o cliente primeiro e, depois, cadastre o teste")
            return redirect('new_test')

        test.client = client

        

        try:
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']

            sdate = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            test.start_date = start_date

            if end_date != '':
                edate = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
                if sdate > edate:
                    messages.error(request, "A data de ínicio tem que anteceder a data de finalização")
                    return redirect('new_test')
                else:
                    test.end_date = end_date

        except Exception as ex:
            print(ex)
            messages.error(request, "Verifique o campo de data")
            return redirect('new_test')

        test.technician = request.POST['technician']
    
        try:
            tk_grade = float(request.POST['tk_range'])
            tr_grade = float(request.POST['tr_range'])
            fb_grade = float(request.POST['fb_range'])

            for param in [tk_grade, tr_grade, fb_grade]:
                if param < 0 or param > 5:
                    messages.error(request, "As notas devem estar entre 0 e 5")
                    return redirect('new_test')

        except Exception:
            messages.error(request, 'Erro com o valor das notas')

        test.tk_grade = tk_grade
        test.tr_grade = tr_grade
        test.fb_grade = fb_grade
        test.tk_comments = request.POST['tk_comments']
        test.tr_comments = request.POST['tr_comments']
        test.fb_comments = request.POST['fb_comments']

        final_grade = (tk_grade + tr_grade + fb_grade)/3
        test.final_grade = round(final_grade, 2)
        test.final_comments = request.POST['final_comments']
        test.contract_id = request.POST['contract_id']

        tests_cl = Test.objects.filter(client_id=client).order_by('-created_at')
        n_tests = tests_cl.count()
        client_grade = 0

        if n_tests >= 2: 
            print(n_tests)
            last_tests = tests_cl[:2]

            for i in last_tests:
                print(i.product_tested)
                client_grade += i.final_grade
                print(client_grade)

            client.grade =  (client_grade + final_grade)/3
        else:
            for i in tests_cl:
                client_grade += i.final_grade

            client_grade = (client_grade+final_grade)/(len(tests_cl)+1)

        client.grade = round(client_grade, 2)
        client.save()
        test.save()

        messages.success(request, 'Teste cadastrado com sucesso')
        return redirect('new_test')

    return render(request, 'tests/new-test.html')


def tests(request):
    return render(request, 'tests/tests.html')


def test_detail(request, test_id):
    return render(request, 'tests/test-detail.html')
