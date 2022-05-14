from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse


def login(request):
    return render(request, 'accountapp/hello.html')