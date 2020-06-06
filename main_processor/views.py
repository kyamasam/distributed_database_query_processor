from django.shortcuts import render

from .forms import QueryForm
# from .models import ParentTable
from .models import ParentTable


def homeview(request):
    tables_list = ParentTable.objects.all()
    columns_list = ParentTable.objects.all()

    if request.method == 'POST':
        print("POST")

        form = QueryForm(request.POST)
        if form.is_valid():
            projection = form.cleaned_data['projection']
            cartesian_product = form.cleaned_data['cartesian_product']
            selection = form.cleaned_data['selection']
            print("rest", projection, cartesian_product)
            errors = []


            # select table
            selection_list = ",".join(selection)
            projection_list = ",".join(projection)
            projection_list = projection_list.replace('"', '')

            parent = ParentTable.objects.filter(table_name=cartesian_product).first()
            child = parent.children_table.filter(fragment_query__contains=selection)
            child = child.first()
            child_table_name = child.child_table_name

            print("child table", child)


            initial_user_query = "SELECT " + projection_list + " FROM " + child_table_name + " WHERE " + selection

            if parent.fragmentation_type != 'horizontal':
                get_url = "http://127.0.0.1:5000/?projection=SELECT " + projection_list + "&cartesian_product= FROM " \
                          + child_table_name + "&selection= " + "&target_database="\
                          + child.database_name
            else:
                get_url = "http://127.0.0.1:5000/?projection=SELECT " + projection_list + "&cartesian_product= FROM " \
                          + child_table_name + "&selection= where " + selection + "&target_database=" \
                          + child.database_name

            context = {
                'projection': projection,
                'cartesian_product': cartesian_product,
                'selection': selection,
                'tables_list': tables_list,
                'columns_list': columns_list,
                'errors': errors,
                'get_url': get_url,
                'initial_user_query':initial_user_query
            }
            print("here is it", context['projection'])

            # return HttpResponse("QUERY OBJECT {} {} {}".format(projection, table, values))
            return render(request, 'master_system/index.html', context)
        return render(
            request, 'master_system/index.html',
            {'form': form, 'tables_list': tables_list, 'columns_list': columns_list}
        )

    else:
        form = QueryForm()
        return render(
            request, 'master_system/index.html',
            {'form': form, 'tables_list': tables_list, 'columns_list': columns_list}
        )
