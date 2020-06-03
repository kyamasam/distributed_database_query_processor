from django.db import models
from django.utils import timezone


# class for creating timestamps in all models
# this class inherits the main model class
# it will be inherited by other classes
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_recent(self):
        difference = timezone.now() - self.created_at
        if difference.days < 1:
            return True
        else:
            return False

    # indicate that this is an abstract class
    class Meta:
        abstract = True


class Application(TimeStampMixin):
    application_name = models.CharField(max_length=255)
    database_name = models.CharField(max_length=255)
    database_password = models.CharField(max_length=255)
    database_host = models.CharField(max_length=255)
    database_port = models.CharField(max_length=255)
    database_connector = models.CharField(max_length=255)

    def __str__(self):
        return self.application_name


class Site(TimeStampMixin):
    site_name = models.CharField(max_length=255)

    def __str__(self):
        return self.site_name


class ParentTable(TimeStampMixin):
    table_name = models.CharField(max_length=255)
    columns = models.CharField(max_length=3000)
    fragmentation_type = models.CharField(max_length=255)

    def columns_as_array(self):
        return self.columns.split(",")

    def __str__(self):
        return self.table_name


class ChildTableFragment(TimeStampMixin):
    parent_table = models.ForeignKey(ParentTable, on_delete=models.CASCADE , related_name="children_table")
    child_table_name = models.CharField(max_length=255)
    fragment_columns = models.CharField(max_length=255)
    fragment_query = models.TextField(max_length=1000)
    database_name = models.CharField(max_length=255)

    def __str__(self):
        return self.child_table_name

