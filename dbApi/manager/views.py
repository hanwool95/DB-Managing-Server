
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import DxSerializer, MedSerializer, LabSerializer, PxSerializer
from django.shortcuts import render

from .models import Dx, Lab, Med, Px

class DxAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Dx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class DxDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Dx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

class LabAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class LabDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

class MedAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Med.objects.all()
    serializer_class = MedSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class MedDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Med.objects.all()
    serializer_class = MedSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

class PxAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Px.objects.all()
    serializedr_class = PxSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class PxDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Px.objects.all()
    serializer_class = PxSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

def index(request):
    return render(request, 'manager/index.html')


def create_concate_db(request):
    pass



def concate_db(request, number):
    if(request.method == "CREATE"):
        pass
