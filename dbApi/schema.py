import graphene
from graphene_django import DjangoObjectType

from gql.models import Ddata, Mdata, Ldata, Pdata


class DdataType(DjangoObjectType):
    class Meta:
        model = Ddata
        fields = ('id', 'client_num', 'gender', 'birth', 'field', 'date', 'first_date', 'd_code', 'd_name', 'd_scode')


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
    Ddata_by_client_num = graphene.List(DdataType, number=graphene.String(required=True))
    all_Mdatas = graphene.List(MdataType)

    # all_Datas 호출시 받게되는 함수. 밑에도 마찬가지로
    def resolve_all_Ddatas(root, info):
        return Ddata.objects.all()

    """
    예시 쿼리
    query {
    allDdatas {
    clientNum
    dCode
    dName
    dScode
    }
    }
    """

    def resolve_Ddata_by_client_num(root, info, number):
        client_num = "Case "+number
        print(client_num)
        try:
            return Ddata.objects.filter(client_num=client_num).all()
        except Ddata.DoesNotExist:
            return None
    """
    query {
    DdataByClientNum(number: "3") {
    date
    dCode
    dName
    dScode
    }
    }
    """

    def resolve_all_Mdatas(root, info):
        return Mdata.objects.all()




schema = graphene.Schema(query=Query)


