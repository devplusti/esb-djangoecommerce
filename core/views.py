# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   TextoExemplo = ['Lorem ipsum dolor sit amet', 'consectetur adipisicing elit', 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.']

   context = {
      'xTitulo': 'minha lojinha',
      'xTexto': TextoExemplo
   }
   return render(request, 'index.html', context)


def contact(request):
   return render(request, 'contact.html')


def product(request):
   return render(request, 'product.html')


def product_list(request):
   return render(request, 'product_list.html')
