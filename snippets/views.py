from django.shortcuts import render
from django.http import HttpResponse


def top(request):
    return  HttpResponse(b"Hello World")

def snippet_new(request):
    return HttpResponse('スペニットの登録')

def snippet_edit(request, snippet_id):
    return HttpResponse('スペニットの編集')

def snippet_detail(request, snippet_id):
    return HttpResponse('スペニットの詳細')