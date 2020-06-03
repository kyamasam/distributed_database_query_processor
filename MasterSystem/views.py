from django.shortcuts import render
from django.http import HttpResponse

from processor import models
from boltons.strutils import pluralize, singularize


# def homeview(request):
#     columns = 'id, name'
#     table = 'students'
#     secondary_tables = ['students']
#     selection = ['campus="chiromo"']
#
#     table = (singularize(table)).capitalize
#     # loop to create selection string
#     selection_string = ''
#     for index, secondary_tables in enumerate(secondary_tables) :
#         # selection_string += '', secondary_tables[index], '.',selection[index]
#         print(secondary_tables[index])
#         print(selection[index])
#         # for SQL
#         sql_query = 'select', columns, 'from ', table, 'where'
#
#     return render(request, "master_system/index.html")
