
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DxSerializer
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Dx

class DxAPI(APIView):
    def get(self, request):
        queryset = Dx.objects.all()
        print("get: ", queryset)
        serializer = DxSerializer(queryset, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, 'manager/index.html')


def create_concate_db(request):
    pass



def concate_db(request, number):
    if(request.method == "CREATE"):
        pass
