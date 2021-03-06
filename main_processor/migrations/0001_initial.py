# Generated by Django 3.0.6 on 2020-06-02 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application_name', models.CharField(max_length=255)),
                ('database_name', models.CharField(max_length=255)),
                ('database_password', models.CharField(max_length=255)),
                ('database_host', models.CharField(max_length=255)),
                ('database_port', models.CharField(max_length=255)),
                ('database_connector', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParentTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('table_name', models.CharField(max_length=255)),
                ('columns', models.CharField(max_length=3000)),
                ('fragmentation_type', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChildTableFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('child_table_name', models.CharField(max_length=255)),
                ('fragment_columns', models.CharField(max_length=255)),
                ('fragment_query', models.TextField(max_length=1000)),
                ('database_name', models.CharField(max_length=255)),
                ('parent_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_table', to='main_processor.ParentTable')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
