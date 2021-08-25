from django.db import models
from accounts.models import Account
from client.models import Client

test_status = (
    ('Finalizado', 'Finalizado'),
    ('Em andamento', 'Em andamento')
)


# Create your models here.
class Test(models.Model):
    class Meta:
        verbose_name = 'Teste'
        verbose_name_plural = 'Testes'

    user = models.ForeignKey(Account, verbose_name='Usário que criou', on_delete=models.SET_NULL, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    product_tested = models.CharField(max_length=20, verbose_name='Produto testado')
    start_date = models.DateField(verbose_name='Data de início')
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)
    end_date = models.DateField(verbose_name='Data de finalização', blank=True, null=True)
    technician = models.CharField(verbose_name="Nome do instalador/técnico", max_length=30, blank=True)
    contract_id = models.CharField(verbose_name="Código do contrato", max_length=50, blank=True)
    status = models.CharField(verbose_name="Status", blank=True, choices=test_status, max_length=20, default='Em andamento')
    tk_grade = models.FloatField(verbose_name="Nota do conhecimento técnico", default=5)
    tk_comments = models.TextField(verbose_name="Comentário sobre conhecimento técnico", max_length=1000, blank=True)
    tr_grade = models.FloatField(verbose_name="Nota do tempo de resposta", default=5)
    tr_comments = models.TextField(verbose_name="Comentário sobre o tempo de resposta", max_length=1000, blank=True)
    fb_grade = models.FloatField(verbose_name="Nota do feedback que o cliente forneceu", default=5)
    fb_comments = models.TextField(verbose_name="Comentário sobre o feedback que o cliente forneceu", max_length=1000, blank=True)
    final_grade = models.FloatField(verbose_name="Nota final", default=5)
    final_comments = models.TextField(verbose_name="Comentários finais", max_length=300, blank=True) 

    def __str__(self) -> str:
        return self.product_tested