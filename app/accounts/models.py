from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.expressions import Value

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must has an email address')

        if not username:
            raise ValueError('User must has an username')

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

UNITS = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C')
)

SEGMENTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
)

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=20, verbose_name='Nome')
    last_name = models.CharField(max_length=20, verbose_name='Sobrenome')
    username = models.CharField(max_length=20, verbose_name='Nome de usuário', unique=True)
    email = models.EmailField(max_length=50, verbose_name='E-mail', unique=True)

    unit = models.CharField(verbose_name="Unidade", max_length=20, choices=UNITS, default='A')
    segment = models.CharField(verbose_name="Segmento", max_length=20, choices=SEGMENTS, default='1')

    #required
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='Última sessão')
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_superadmin = models.BooleanField(default=False, verbose_name='Super admin')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_staff= models.BooleanField(default=False, verbose_name='Staff')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True