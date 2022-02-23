from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError
from django.template import loader
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from users.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
# import hashlib
# import secrets

# Create your views here.
User = get_user_model()


# def scramble(password: str):
#     """Hash and salt the given password"""
#     salt = secrets.token_hex(16)
#     return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


def register(request):
    next = request.GET.get('next', '/')
    try:
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request, username=username, password=password)
        try:
            login(request, auth_user)
            return HttpResponseRedirect(next)
        except:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect(next)
    except (KeyError):
        messages.error(request, 'Invalid credentials')
        # return render(request, '/', { 'message': "Invalid username or password. Please try again." })


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         email = request.POST['email']
#         birthdate = request.POST['birthdate']

#         print("----------------- register called")
#         print(username)
#         print(password)
#         print(firstname)
#         print(lastname)
#         print(email)
#         print(birthdate)
#         try:
#             user = get_object_or_404(User, username=username)
#         except:
#             pass
#         messages.success(request,
#                          f'Your account has been created! You can now login!')
#         return redirect('login')
#     else:
#         return render(request, 'users/register.html')


@api_view(['GET', 'POST', 'PATCH'])
def register(request):
    if request.method == 'GET':
        users = User.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            users = users.filter(title__icontains=title)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

        # 'safe=False' for objects serialization

    # elif request.method == 'POST':
    #     user_data = JSONParser().parse(request)
    #     # print(user_data)
    #     user_serializer = UserSerializer(data=user_data)
    #     if user_serializer.is_valid():
    #         user_serializer.save()
    #         return JsonResponse(user_serializer.data,
    #                             status=status.HTTP_201_CREATED)
    #     return JsonResponse(user_serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'POST':
    #     def register(request):
    #         if request.method == 'POST':
    #             user_data = User.object.body(
    #                 username=request.POST['username'],
    #                 password=request.POST['password'],
    #                 first_name=request.POST['firstname'],
    #                 last_name=request.POST['lastname'],
    #                 email=request.POST['email'],
    #                 birthdate=request.POST['birthdate']
    #             )
    #             user_serializer = UserSerializer(data=user_data)
    #             if user_serializer.is_valid():
    #                 # user_serializer.password = scramble(user_data.password)
    #                 user_serializer.save()
    #                 return HttpResponseRedirect(next)
    #             return HttpResponseRedirect(next)

    elif request.method == 'PATCH':
        count = User.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} users were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        def request(request):
            if request.method == 'POST':
                form = UserSerializer(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=username,
                                        password=raw_password)
                    login(request, user)
                    return redirect('home')
            else:
                form = UserSerializer()
            return render(request, 'users/register.html')


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        passport = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The Passport does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UserSerializer(passport)
        return JsonResponse(user_serializer.data)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(passport, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        User.delete()
        return JsonResponse({'message': 'Passport was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_list_published(request):
    users = User.objects.filter(published=True)

    if request.method == 'GET':
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
