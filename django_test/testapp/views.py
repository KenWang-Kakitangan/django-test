
from django.shortcuts import render

from django.db import models
from django.http import HttpResponse
from django.db import connection

# Create your views here.

def CreateDynamicModel (table_name):
    class Meta:
            db_table = '%s_table' % table_name.lower()

    attrs = {'__module__': 'testapp', 'Meta': Meta, 'db_tablespace': 'tables'} 

    # specify any other class attributes here. E.g. you can specify extra fields:
    attrs.update({'my_field': models.CharField(max_length=100)})

    newclass = type(str(table_name), (models.Model,), attrs)

    return newclass

def DynamicModel (request):
    myModelA = CreateDynamicModel('A')
    myModelB = CreateDynamicModel('B')

    with connection.schema_editor() as editor:
            editor.create_model(myModelA)
            editor.create_model(myModelB)

    return HttpResponse('OK');

