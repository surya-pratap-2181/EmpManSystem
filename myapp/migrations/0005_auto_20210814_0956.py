# Generated by Django 3.2.5 on 2021-08-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_user_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_exit',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emp_ctc',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='manager_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='remark',
            field=models.TextField(null=True),
        ),
    ]
