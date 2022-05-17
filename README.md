<p align="center">
    <img src="./static/images/logo.png" alt="Unform" />
</p>

<h1 align="center">TestHunter Web App</h1>

<h1 align="center">
    <a href="https://https://www.djangoproject.com//">🔗 Django</a>
</h1>
<p align="center">🚀 Aplicação Web de um sistema para gerenciamento de testes de campo para produtos eletrônicos desenvolvido com o framework Django</p>

<p align="center">
    <img src="https://img.shields.io/badge/django%20versions-3.1-green" alt="Unform" />
    <img src="https://img.shields.io/badge/license-MIT-green" alt="Unform" />
</p>



<p align="center">
 <a href="#objetivo">Objetivo</a> •
 <a href="#como-utilizar">Como utilizar</a> • 
 <a href="#sreenshots">Sreenshots</a> • 
 <a href="#licenca">Licença</a> • 
 <a href="#autor">Autor</a>
</p>

# Objetivo

Esta aplicação tem como objetivo gerenciar testes de campo com clientes durante o desenvolvimento de produtos eletrônicos:

- Cadastro de cliente
- Cadastro do teste
    - Descrição
    - Categoria
    - Duração
    - Status
- Avaliação do teste de campo
- Avaliação do cliente
- Classificação dos clientes com base nos testes realizados

A Aplicação foi desenvolvida com base em um [curso na Udemy](https://www.udemy.com/course/django-ecommerce-project-based-course-python-django-web-development/) com alguns recursos extras. 

## Como utilizar

Para utilizar a aplicação, clone o repositório, instale os pacotes necessários e inicie a aplicação:

```shell
pip install requirements.txt
```

```shell
python manage.py runserver
```

Acesse a url da aplicação:

```
127.0.0.1:8000/
```

Para criar um adminstrador e poder acessar as opções de admininstrador, execute o seguinte comando no terminal e siga a instruções que serão impressas:

```shell
python manage.py createsuperuser
```
Após o perfil de adminstrador ter sido criado, acesso o seguinte URL para poder acessar os recursos de admininstrador:

```
127.0.0.1:8000/admin/
```


## Sreenshots

Dashboard inicial do usuário:

<p align="center">
    <img src="screenshots/test_hunter_dashboard.png" alt="Unform" />
</p>

Dados do teste:
<p align="center">
    <img src="screenshots/test-hunter-carousel-3.png" alt="Unform" />
</p>

Testes realizados:
<p align="center">
    <img src="screenshots/test_hunter.png" alt="Unform" />
</p>

Classificação dos clientes:
<p align="center">
    <img src="screenshots/test-hunter-carousel-4.png" alt="Unform" />
</p>

## Licença

MIT © Rafael Hiller

## Autor

Feito por Rafael Hiller.

[![Linkedin Badge](https://img.shields.io/badge/-Rafael-blue?style=flat-square&logo=Linkedin&logoColor=white&link=hhttps://www.linkedin.com/in/rafael-hiller-0aa187133/)](https://www.linkedin.com/in/rafael-hiller-0aa187133/) 