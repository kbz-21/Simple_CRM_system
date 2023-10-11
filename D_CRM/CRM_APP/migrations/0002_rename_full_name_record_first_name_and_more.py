# Generated by Django 4.1 on 2023-09-17 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_APP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='Full_Name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='ID',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='record',
            name='student_id',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='Email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
