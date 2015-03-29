from django.db import models

def CreateDynamicModel (table_name):
    class Meta:
            db_table = '%s_table' % table_name.lower()

    attrs = {'__module__': 'testapp', 'Meta': Meta, 'db_tablespace': 'tables'} 

    # specify any other class attributes here. E.g. you can specify extra fields:
    attrs.update({'my_field': models.CharField(max_length=100)})
    newclass = type(str(table_name), (models.Model,), attrs)


myModelA = CreateDynamicModel('A')
myModelB = CreateDynamicModel('B')