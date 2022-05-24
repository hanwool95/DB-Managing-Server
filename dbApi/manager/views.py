
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import DxSerializer
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse

from .models import Dx

class DxAPI(APIView):
    def get(self, request):
        queryset = Dx.objects.all()
        print("get: ", queryset)
        serializer = DxSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response("wrong parameter", status=status.HTTP_400_BAD_REQUEST)

class DxNumberingAPI(APIView):
    def get(self, request, number):
        queryset = Dx.objects.get(id=number)
        print("get: ", queryset)
        serializer = DxSerializer(queryset)
        return Response(serializer.data)

    def patch(self, request, number):
        queryset = Dx.objects.get(id=number)
        serializer = DxSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response("wrong parameter", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, number):
        Dx.objects.get(id=number).delete()
        return Response("delete")


def index(request):
    return render(request, 'manager/index.html')


def create_concate_db(request):
    pass



def concate_db(request, number):
    if(request.method == "CREATE"):
        pass
