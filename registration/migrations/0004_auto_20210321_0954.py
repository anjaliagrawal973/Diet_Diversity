# Generated by Django 3.0.8 on 2021-03-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20210321_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='ICDScenteraddress',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='ICDScentercontact',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='annualincome',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='cuid',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='education',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='fatherage',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='fatherbirthdate',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='fathername',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='motherage',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='motherbirthdate',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='mothername',
        ),
        migrations.RemoveField(
            model_name='smchildparentsregister',
            name='occupation',
        ),
        migrations.AddField(
            model_name='smchildparentsregister',
            name='childbirthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='smchildparentsregister',
            name='childfirstname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='smchildparentsregister',
            name='childis',
            field=models.CharField(choices=[('SAM', 'SAM'), ('MAM', 'MAM')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='smchildparentsregister',
            name='childlastname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]