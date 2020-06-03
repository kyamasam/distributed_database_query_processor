from django.contrib import admin
from .models import *
admin.site.register(ChildTableFragment)
admin.site.register(Application)
admin.site.register(ParentTable)