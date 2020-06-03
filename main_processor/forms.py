from django import forms
from .models import ParentTable


class QueryForm(forms.Form):
    cols_list = list(ParentTable.objects.values_list('columns', flat=True))
    cols_list_split = []
    cols_list_pairs = []
    for i in cols_list:
        # separate with commas
        cols_list_split += i.split(",")

    # create a key value pair with column names
    for i in cols_list_split:
        cols_list_pairs.append((i, i))

    parent_tables = ParentTable.objects.values_list('table_name', 'id')
    columns_list = ParentTable.objects.values_list('columns', 'columns')
    projection = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=cols_list_pairs)
    cartesian_product = forms.CharField(label="table", )
    selection = forms.CharField(label="values", )


