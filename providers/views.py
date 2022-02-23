from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError
from django.template import loader

# Create your views here.
Provider = get_user_model()


def register(request):
    next = request.GET.get('next', '/')
    try:
        code = request.POST['code']
        password = request.POST['password']
        auth_user = authenticate(request, code=code, password=password)
        try:
            login(request, auth_user)
            return HttpResponseRedirect(next)
        except:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect(next)
    except (KeyError):
        messages.error(request, 'Invalid credentials')
        # return render(request, '/', { 'message': "Invalid username or password. Please try again." })


def register(request):
    if request.method == 'POST':
        code = request.POST['code']
        password = request.POST['password']
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']

        print("----------------- register called")
        print(code)
        print(password)
        print(name)
        print(address)
        print(email)

        # try:
        #     user = get_object_or_404(User, username=username)
        # except:
        #     pass

        messages.success(request,
                         f'Your account has been created! You can now login!')
        return redirect('login')
    else:
        return render(request, 'users/register.html')
