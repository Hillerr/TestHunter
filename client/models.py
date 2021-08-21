from django.db import models
from django.db.models.fields.related import ForeignKey
from accounts.models import Account

business_type = (
    ('Provedor', 'Provedor'),
    ('Integrador', 'Integrador'),
    ('Cliente Final', 'Cliente Final')
)

# Create your models here.
class Client(models.Model):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    user = models.ForeignKey(Account, verbose_name="Usuário que cadastrou", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(verbose_name="Nome do cliente", max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(verbose_name="Telefone", max_length=20)
    state = models.CharField(verbose_name="Estado", max_length=50)
    city = models.CharField(verbose_name="Cidade", max_length=50)
    grade = models.DecimalField(verbose_name="Nota", max_digits=3, decimal_places=2, blank=True, null=True)
    code = models.CharField(verbose_name="CPF ou CNPJ", max_length=15, unique=True)
    created_at = models.DateTimeField(verbose_name="Data de cadastro", auto_now=True)
    last_update = models.DateTimeField(verbose_name="Última atualização", auto_now_add=True)
    business = models.CharField(verbose_name="Tipo de cliente", choices=business_type, max_length=50)

    def __str__(self) -> str:
        return self.name
