import graphene
from graphene_django import DjangoObjectType

from gql.models import Ddata, Mdata, Ldata, Pdata


class DdataType(DjangoObjectType):
    class Meta:
        model = Ddata
        fields = ('id', 'client_num', 'gender', 'birth', 'field', 'date', 'first_date', 'd_code', 'd_name', 'ds_code')


class MdataType(DjangoObjectType):
    class Meta:
        model = Mdata
        fields = ('id', 'client_num', 'gender', 'birth', 'field', 'date', 'm_iname', 'm_oname', 'm_result')


class LdataType(DjangoObjectType):
    class Meta:
        model = Ldata
        fields = ('id', 'client_num', 'gender', 'birth', 'field', 'date', 'l_name', 'l_float', 'l_pm', 'l_result')


class PdataType(DjangoObjectType):
    class Meta:
        model = Pdata
        fields = ('id', 'client_num', 'gender', 'birth', 'date', 'p_name', 'p_result')


class Query(graphene.ObjectType):
    all_Ddatas = graphene.List(DdataType)
    Ddata_by_client_num = graphene.Field(DdataType, client_num=graphene.String(required=True))

    # all_Datas 호출시 받게되는 함수. 밑에도 마찬가지로 ㄱㄷ재ㅣㅍㄷfmf dldydgotj ghcnfgka.
    def resolve_all_Ddatas(root, info):
        return Ddata.objects.select_related('client_num').all()

    def resolve_Ddata_by_number(root, info, number):
        client_num = "Case "+number
        try:
            return Ddata.objects.get(client_num=client_num)
        except Ddata.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)


