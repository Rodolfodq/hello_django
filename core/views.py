from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome, idade):
    return HttpResponse('<h1>Hello {} de {}!</h1>'.format(nome, idade))