import datetime
from .models import Test
from client.models import Client


def validate_date(test, request):
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']

    if start_date != '' and end_date == '':
        test.start_date = start_date
        test.end_date = None

    elif end_date != '' and start_date == '':
        test.end_date = end_date
        test.start_date = None

    elif end_date != '' and start_date != '':
        edate = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        sdate = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        if sdate > edate:
            raise ValueError("A data de ínicio tem que anteceder a data de finalização")
        else:
            test.end_date = end_date
            test.start_date = start_date


def validate_grades(test, client, request):
    tk_grade = float(request.POST['tk_range'])
    tr_grade = float(request.POST['tr_range'])
    fb_grade = float(request.POST['fb_range'])

    for param in [tk_grade, tr_grade, fb_grade]:
        if param < 0 or param > 5:
            raise ValueError("As notas devem estar entre 0 e 5")

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
        last_tests = tests_cl[:2]

        for i in last_tests:
            client_grade += i.final_grade

        client_grade =  (client_grade + final_grade)/3
    else:
        for i in tests_cl:
            client_grade += i.final_grade

        client_grade = (client_grade+final_grade)/(len(tests_cl)+1)

    client.grade = round(client_grade, 2)


def save_test(request):
        test = Test()
        test.user = request.user
        test.product_tested = request.POST['product_tested']
        client_code = request.POST['client_code']

        try: 
            client = Client.objects.get(code=client_code)
        except Client.DoesNotExist:
            raise ValueError(f"Não foi encontrado nenhum cliente com o CPF/CNPJ {client_code}. Por favor, cadastre o cliente primeiro e, depois, cadastre o teste")

        test.client = client
        
        try:
            validate_date(test, request)

        except Exception as ex:
            raise ValueError("Verifique o campo de data")

        test.technician = request.POST['technician']

        if request.POST['quantity'] != '':
                test.quantity = request.POST['quantity']
    
        validate_grades(test, client, request)

        client.save()
        test.save()


