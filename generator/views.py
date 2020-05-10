from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password_generate(request):
    length = int(request.GET.get("length"))
    capital_alphabet = request.GET.get("capital_alphabet")
    special_character = request.GET.get("special_character")
    alpha_numeric = request.GET.get("alpha_numeric")
    characters = list('abcdefghijklmnopqrstuvwxyz')
    print(capital_alphabet)
    password = ''
    if capital_alphabet=='on':
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if special_character=='on':
        characters.extend('!@#$%^&*()_+')
    if alpha_numeric=='on':
        characters.extend('0123456789')
    for x in range(length):
        password+=random.choice(characters)
    return render(request,'generator/password.html' , {"password": password})

def about(request):
    # return HttpResponse('this site is created by me')
    return render(request,'generator/about.html')
