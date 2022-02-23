from django.shortcuts import render
import datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from passports.models import Passport
from passports.serializers import PassportSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "passports/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Passport.objects.all()
    return render(request, "passports/index.html", {'passports': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'passports/index.html'

    def get(self, request):
        queryset = Passport.objects.all()
        return Response({'passports': queryset})


class list_all_passports(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'passports/passport_list.html'

    def get(self, request):
        queryset = Passport.objects.all()
        return Response({'passports': queryset})


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def passport_list(request):
    if request.method == 'GET':
        passports = Passport.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            passports = passports.filter(title__icontains=title)

        passports_serializer = PassportSerializer(passports, many=True)
        return JsonResponse(passports_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        passport_data = JSONParser().parse(request)
        passport_serializer = PassportSerializer(data=passport_data)
        if passport_serializer.is_valid():
            passport_serializer.save()
            return JsonResponse(passport_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(passport_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Passport.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Passports were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def passport_detail(request, pk):
    try:
        passport = Passport.objects.get(pk=pk)
    except Passport.DoesNotExist:
        return JsonResponse({'message': 'The Passport does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        passport_serializer = PassportSerializer(passport)
        return JsonResponse(passport_serializer.data)

    elif request.method == 'PUT':
        passport_data = JSONParser().parse(request)
        passport_serializer = PassportSerializer(passport, data=passport_data)
        if passport_serializer.is_valid():
            passport_serializer.save()
            return JsonResponse(passport_serializer.data)
        return JsonResponse(passport_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Passport.delete()
        return JsonResponse({'message': 'Passport was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def passport_list_published(request):
    passports = Passport.objects.filter(published=True)

    if request.method == 'GET':
        passports_serializer = PassportSerializer(passports, many=True)
        return JsonResponse(passports_serializer.data, safe=False)
