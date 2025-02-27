from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
# Create your views here.

users = ['dasha', 'Vanya', 'Eyogurty','Semenka']
info = {}

# def sign_up_by_html(request):
#     if request.method == 'POST':
#         username =request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')
#         if password == repeat_password and int(age) >= 18 and username not in users:
#             return HttpResponse(f'Приветствуем, {username}!')
#         print(f'Username: {username}, password:{password}, repeat_password: {repeat_password}, age :{age}')
#         if password != repeat_password and int(age) >= 18 and username not in users:
#             info["error"]='Пароли не совпадают'
#             # return HttpResponse(f'Пароли не совпадают')
#         if password == repeat_password and int(age) < 18 and username not in users:
#             info["error"] ='Вы должны быть старше 18'
#         if password == repeat_password and int(age) >= 18 and username in users:
#             info["error"]='Пользователь уже существует'
#     context = {
#         'info': info,
#     }
#     return render(request, 'fifth_task/registration_page.html',context)

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                return HttpResponse(f'Приветствуем, {username}!')
            print(f'Username: {username}, password:{password}, repeat_password: {repeat_password}, age :{age}')
            if password != repeat_password and int(age) >= 18 and username not in users:
                info["error"] = 'Пароли не совпадают'
            if password == repeat_password and int(age) < 18 and username not in users:
                info["error"] = 'Вы должны быть старше 18'
            if password == repeat_password and int(age) >= 18 and username in users:
                info["error"] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    context = {
        'info': info,
        'form' : form,
    }
    return render(request, 'fifth_task/registration_page.html',context)