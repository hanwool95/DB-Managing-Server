from django.contrib import admin
from gql.models import Ddata, Mdata, Ldata, Pdata

admin.site.register(Mdata)
admin.site.register(Ddata)
admin.site.register(Pdata)
admin.site.register(Ldata)

