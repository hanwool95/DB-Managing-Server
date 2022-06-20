
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import DxSerializer, MedSerializer, LabSerializer, PxSerializer, FxSerializer, EventSerializer
from django.shortcuts import render
from django.http import JsonResponse

from .models import Dx, Lab, Med, Px, Fx, Event

class DxAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Dx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class DxCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Dx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Dx.objects.filter(number=case)

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

class LabCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Lab.objects.filter(number=case)

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

class MedCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Med.objects.all()
    serializer_class = MedSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Med.objects.filter(number=case)

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

class PxCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Px.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Px.objects.filter(number=case)

class PxDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Px.objects.all()
    serializer_class = PxSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)

class FxAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Fx.objects.all()
    serializer_class = FxSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class FxCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Fx.objects.all()
    serializer_class = DxSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Fx.objects.filter(number=case)

class FxDetailAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Fx.objects.all()
    serializer_class = FxSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, partial=True)

    def patch(self, request: Request, pk: int):
        return self.update(request, partial=True)

    def delete(self, request: Request, pk: int):
        return self.destroy(request)


class EventAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class EventCaseAPI(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericAPIView, DestroyModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.list(request)

    def post(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.create(request)

    def delete(self, request: Request, number: int):
        self.set_query_by_number(number)
        return self.destroy(request)

    def set_query_by_number(self, number: int):
        case = 'Case ' + str(number)
        self.queryset = Event.objects.filter(number=case)


def index(request):
    return render(request, 'manager/index.html')


def create_concate_db(request):
    pass


def total_data(request, case_num: int):
    case_num_string = "Case " + str(case_num)
    events = Event.objects.filter(number=case_num_string)
    dxs = Dx.objects.filter(number=case_num_string)
    labs = Lab.objects.filter(number=case_num_string)
    meds = Med.objects.filter(number=case_num_string)
    fxs = Fx.objects.filter(number=case_num_string)
    pxs = Px.objects.filter(number=case_num_string)

    result_dict = {
        'caseNum' : case_num_string,
        'gender' : labs[0].sex,
        'birthDate': labs[0].birth,
        'events': {},
        'event_dates': []
    }
    prev_date = events[0].date
    for event in events:
        date = event.date
        result_dict['event_dates'].append(date)

        separate_dict = {'dx': [], 'lab': [], 'med': [], 'firsts': [], 'afters': []}

        filtered_dxs = dxs.filter(date=date)
        for dx in filtered_dxs:
            dx_dict = {
                'first_date': dx.first_date,
                'diag_code': dx.diagnostic_code,
                'diag_name': dx.diagnostic_name,
                'ICD10_code': dx.icd10_code

            }
            separate_dict['dx'].append(dx_dict)

        if prev_date == date:
            filtered_labs = labs.filter(date=date)
        else:
            filtered_labs = labs.filter(date__lte=date, date__gt=prev_date)
        for lab in filtered_labs:
            lab_type = "Text"
            if lab.result_numerical:
                lab_type = "Number"
            elif lab.result_negpos:
                lab_type = "NegPos"
            lab_dict = {
                'lab_name': lab.test_name,
                'lab_type': lab_type,
                'lab_num': lab.result_numerical,
                'lab_pn': lab.result_negpos,
                'lab_text': lab.result_total

            }
            separate_dict['lab'].append(lab_dict)

        filtered_meds = meds.filter(date=date)
        for med in filtered_meds:
            med_dict = {
                'med_name_ingr': med.name_ingredient,
                'name_normal': med.name_normal,
                'prescrpition': med.prescription
            }
            separate_dict['med'].append(med_dict)

        filtered_fxs = fxs.filter(date=date)
        for fx in filtered_fxs:
            separate_dict['afters'].append(fx.format_content)

        filtered_pxs = pxs.filter(date=date)
        for px in filtered_pxs:
            separate_dict['firsts'].append(px.format_content)

        prev_date = date
        result_dict['events'][str(date)] = separate_dict

    return JsonResponse(result_dict)




def concate_db(request, number):
    if(request.method == "CREATE"):
        pass
