# Generated by Django 3.2.5 on 2021-08-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_remark_user_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_exit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='manager_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
