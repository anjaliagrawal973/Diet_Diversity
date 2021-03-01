# Generated by Django 3.0.8 on 2021-01-07 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('weightunit', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('heightunit', models.CharField(max_length=20)),
                ('bmi', models.IntegerField()),
                ('waist', models.IntegerField()),
                ('waistunit', models.CharField(max_length=20)),
                ('hip', models.IntegerField()),
                ('hipunit', models.CharField(max_length=20)),
                ('whratio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bulk_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('dob', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DailyScheduleForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sleepfrom', models.TimeField()),
                ('sleepto', models.TimeField()),
                ('eatfrom', models.TimeField()),
                ('eatto', models.TimeField()),
                ('studyfrom', models.TimeField()),
                ('studyto', models.TimeField()),
                ('playfrom', models.TimeField()),
                ('playto', models.TimeField()),
                ('housework', models.CharField(max_length=500)),
                ('activities', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DietModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealtype', models.CharField(max_length=200)),
                ('timefrom', models.TimeField()),
                ('timeto', models.TimeField()),
                ('rotiquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('rotiunit', models.CharField(blank=True, max_length=200, null=True)),
                ('ricequantity', models.IntegerField(blank=True, default=0, null=True)),
                ('riceunit', models.CharField(blank=True, max_length=200, null=True)),
                ('pohaquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('pohaunit', models.CharField(blank=True, max_length=200, null=True)),
                ('upmaquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('upmaunit', models.CharField(blank=True, max_length=200, null=True)),
                ('teaquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('teaunit', models.CharField(blank=True, max_length=200, null=True)),
                ('coffeequantity', models.IntegerField(blank=True, default=0, null=True)),
                ('coffeeunit', models.CharField(blank=True, max_length=200, null=True)),
                ('milkquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('milkunit', models.CharField(blank=True, max_length=200, null=True)),
                ('vadaquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('biscuitquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('dalquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('dalunit', models.CharField(blank=True, max_length=200, null=True)),
                ('gujratidalquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('gujratidalunit', models.CharField(blank=True, max_length=200, null=True)),
                ('toordalquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('toordalunit', models.CharField(blank=True, max_length=200, null=True)),
                ('moongdalquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('moongdalunit', models.CharField(blank=True, max_length=200, null=True)),
                ('palakquantity', models.IntegerField(blank=True, default=0, null=True)),
                ('palakunit', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('Document', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='EatTodayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodhabbits', models.CharField(max_length=200)),
                ('foodallergies', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='image_up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInformationForms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('year', models.CharField(max_length=4)),
                ('month', models.CharField(max_length=2)),
                ('days', models.CharField(max_length=2)),
                ('fathername', models.CharField(max_length=200)),
                ('mothername', models.CharField(max_length=200)),
                ('contactnumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('profileimage', models.ImageField(upload_to='profileimages/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalExpert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SupportMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('mentortype', models.CharField(choices=[('Head Mentor', 'Head Mentor'), ('Support Mentor', 'Support Mentor')], default=False, max_length=20)),
                ('category', models.CharField(choices=[('Parent', 'Parent'), ('Teacher', 'Teacher'), ('Student', 'Student')], default=False, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('contact', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=10))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolCoordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('schoolname', models.CharField(max_length=200)),
                ('personaladdress', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(max_length=200, null=True)),
                ('institute', models.CharField(choices=[('Organization', 'Organization'), ('College', 'College'), ('School', 'School')], default=False, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCoordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MukhyaSevika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('personaladdress', models.CharField(max_length=200, null=True)),
                ('anganwadinumber', models.IntegerField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HeadMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('mentortype', models.CharField(choices=[('Head Mentor', 'Head Mentor'), ('Support Mentor', 'Support Mentor')], default=False, max_length=20)),
                ('institute', models.CharField(choices=[('Organization', 'Organization'), ('College', 'College'), ('School', 'School')], default=False, max_length=20)),
                ('qualification', models.CharField(choices=[('BSc', 'BSc'), ('BSW', 'BSW')], default=False, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnganwadiWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('anganwadiname', models.CharField(max_length=200, null=True)),
                ('personaladdress', models.CharField(max_length=200, null=True)),
                ('anganwadiaddress', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
