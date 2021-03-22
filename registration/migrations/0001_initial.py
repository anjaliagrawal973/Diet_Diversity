# Generated by Django 3.0.8 on 2021-03-21 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcentForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concent', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uid', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('nutrileader', models.CharField(choices=[('Nutri-Leader', 'Nutri-Leader'), ('School-Student', 'School-Student')], default=False, max_length=20)),
                ('contact', models.CharField(blank=True, max_length=25500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SMChildParentsRegister',
            fields=[
                ('uid', models.CharField(default=False, max_length=255, primary_key=True, serialize=False)),
                ('mothername', models.CharField(max_length=255)),
                ('fathername', models.CharField(max_length=255)),
                ('motherbirthdate', models.CharField(max_length=255)),
                ('fatherbirthdate', models.CharField(max_length=255)),
                ('motherage', models.IntegerField()),
                ('fatherage', models.IntegerField()),
                ('personalcontact', models.CharField(max_length=200)),
                ('ICDSname', models.CharField(max_length=200)),
                ('ICDScenteraddress', models.CharField(max_length=200)),
                ('ICDScentercontact', models.CharField(max_length=200)),
                ('occupation', models.CharField(choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2550)),
                ('education', models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=255, null=True)),
                ('annualincome', models.CharField(choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=255, null=True)),
                ('cuid', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SMChild',
            fields=[
                ('uid', models.CharField(default=False, max_length=255, primary_key=True, serialize=False)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('age', models.CharField(max_length=255)),
                ('personalcontact', models.CharField(max_length=200)),
                ('ICDSname', models.CharField(max_length=200)),
                ('ICDScenteraddress', models.CharField(max_length=200)),
                ('ICDScentercontact', models.CharField(max_length=200)),
                ('weight', models.IntegerField()),
                ('weightunit', models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255)),
                ('height', models.IntegerField()),
                ('heightunit', models.CharField(choices=[('feet', 'feet'), ('inches', 'inches'), ('cms', 'cms'), ('inches', 'inches')], max_length=50)),
                ('bmi', models.DecimalField(decimal_places=3, max_digits=10)),
                ('waist', models.IntegerField(null=True)),
                ('waistunit', models.CharField(choices=[('cms', 'cms'), ('inches', 'inches')], max_length=20)),
                ('hip', models.IntegerField(null=True)),
                ('hipunit', models.CharField(choices=[('cms', 'cms'), ('inches', 'inches')], max_length=20)),
                ('whratio', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('whratioderived', models.IntegerField(null=True)),
                ('foodhabits', models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=20, null=True)),
                ('uploaded_photo', models.FileField(upload_to='smchilddocuments/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolStudentParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=False, max_length=255)),
                ('birthdate', models.CharField(max_length=2000, null=True)),
                ('age', models.CharField(blank=True, max_length=200)),
                ('schooladdress', models.CharField(max_length=2000, null=True)),
                ('schoolcontact', models.CharField(blank=True, max_length=25500)),
                ('education', models.CharField(blank=True, choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=2000)),
                ('occupation', models.CharField(blank=True, choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2000)),
                ('annualincome', models.CharField(blank=True, choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=25500)),
                ('schoolcoordinatorincharge', models.CharField(blank=True, max_length=25500)),
                ('foodhabits', models.CharField(blank=True, choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=25500)),
                ('profile_photo', models.ImageField(blank=True, upload_to='SchoolStudentParent/%Y/%m/%d')),
                ('contact', models.CharField(blank=True, max_length=10)),
                ('schoolname', models.CharField(max_length=200)),
                ('personaladdress', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolCoordinator',
            fields=[
                ('uid', models.CharField(default=False, max_length=255, primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=25500)),
                ('schoolname', models.CharField(max_length=2000)),
                ('schoolcontact', models.CharField(blank=True, max_length=25500)),
                ('position', models.CharField(choices=[('teaching-staff', 'Teaching Staff'), ('non-teaching-staff', 'Non-Teaching Staff'), ('principal', 'Principal')], max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NutriGardenExpert',
            fields=[
                ('uid', models.CharField(default=False, max_length=255, primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MukhyaSevika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=False, max_length=255)),
                ('ICDSname', models.CharField(max_length=2000, null=True)),
                ('ICDScenteraddress', models.CharField(max_length=2000, null=True)),
                ('ICDScontact', models.CharField(max_length=2000, null=True)),
                ('contact', models.CharField(blank=True, max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('uid', models.CharField(default=False, max_length=255, primary_key=True, serialize=False)),
                ('contact', models.CharField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnganwadiWorkersRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=False, max_length=255)),
                ('contact', models.CharField(blank=True, max_length=25500)),
                ('ICDSname', models.CharField(max_length=2000, null=True)),
                ('ICDScenteraddress', models.CharField(max_length=2000, null=True)),
                ('ICDScontact', models.CharField(max_length=2000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnemicPregnantWoman',
            fields=[
                ('uid', models.CharField(default=False, max_length=255, primary_key=True, serialize=False)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField()),
                ('personalcontact', models.CharField(max_length=200)),
                ('ICDSname', models.CharField(max_length=200)),
                ('ICDScenteraddress', models.CharField(max_length=200)),
                ('ICDScentercontact', models.CharField(max_length=200)),
                ('occupation', models.CharField(choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2550)),
                ('education', models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=255, null=True)),
                ('annualincome', models.CharField(choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=255, null=True)),
                ('weight', models.IntegerField()),
                ('weightunit', models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255)),
                ('height', models.IntegerField()),
                ('heightunit', models.CharField(choices=[('feet', 'feet'), ('inches', 'inches'), ('cms', 'cms'), ('inches', 'inches')], max_length=50)),
                ('bmi', models.DecimalField(decimal_places=3, max_digits=10)),
                ('waist', models.IntegerField(null=True)),
                ('waistunit', models.CharField(choices=[('cms', 'cms'), ('inches', 'inches')], max_length=20)),
                ('hip', models.IntegerField(null=True)),
                ('hipunit', models.CharField(choices=[('cms', 'cms'), ('inches', 'inches')], max_length=20)),
                ('whratio', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('whratioderived', models.IntegerField(null=True)),
                ('foodhabits', models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=20, null=True)),
                ('uploaded_photo', models.FileField(upload_to='anemicpregnantwoman/%Y/%m/%d')),
                ('feedback', models.CharField(max_length=2550)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnemicLactatingMother',
            fields=[
                ('uid', models.CharField(default=False, max_length=255, primary_key=True, serialize=False)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField()),
                ('personalcontact', models.CharField(max_length=200)),
                ('ICDSname', models.CharField(max_length=200)),
                ('ICDScenteraddress', models.CharField(max_length=200)),
                ('ICDScentercontact', models.CharField(max_length=200)),
                ('occupation', models.CharField(choices=[('Legislators,Senior Officials & Managers', 'Legislators,Senior Officials & Managers'), ('Professionals', 'Professionals'), ('Technicians and Associate Professionals', 'Technicians and Associate Professionals'), ('Clerks', 'Clerks'), ('Skilled workers and Shop & Market sales workers ', 'Skilled workers and Shop & Market sales workers '), ('Skilled Agricultural', 'Skilled Agricultural and Fishery workers'), ('Craft and Related Trade Workers', 'Craft and Related Trade Workers'), ('Plant and Machine Operators and Assemblers', 'Plant and Machine Operators and Assemblers'), ('Elementary Occupation', 'Elementary Occupation'), ('Security guard', 'Security guard'), ('Housekeeper or Housemaid', 'Housekeeper or Housemaid'), ('Nurse', 'Nurse'), ('Anganwadi Worker', 'Anganwadi Worker'), ('Retired', 'Retired'), ('Others', 'Others')], max_length=2550)),
                ('education', models.CharField(choices=[('Professionaldegree', 'Professionaldegree'), ('Graduate', 'Graduate (Bachelors)'), ('Middleschool', 'Middle school (5th to 10th std)'), ('Primaryschool', 'Primary school (1st to 4th std)'), ('Illiterate', 'Illiterate (No education)')], max_length=255, null=True)),
                ('annualincome', models.CharField(choices=[('199,862', '199,862'), ('99,931-199,861', '99,931-199,861'), ('74,755-99,930', '74,755-99,930'), ('49,962-74,755', '49,962-74,755'), ('29,973-49,961', '29,973-49,961'), ('10,002-29,97', '10,002-29,97'), ('10,001', '10,001')], max_length=255, null=True)),
                ('weight', models.IntegerField()),
                ('weightunit', models.CharField(choices=[('kgs', 'kgs'), ('lbs', 'lbs')], max_length=255)),
                ('height', models.IntegerField()),
                ('heightunit', models.CharField(choices=[('feet', 'feet'), ('inches', 'inches'), ('cms', 'cms'), ('inches', 'inches')], max_length=50)),
                ('bmi', models.DecimalField(decimal_places=3, max_digits=10)),
                ('waist', models.IntegerField(null=True)),
                ('waistunit', models.CharField(choices=[('cms', 'cms'), ('inches', 'inches')], max_length=20)),
                ('hip', models.IntegerField(null=True)),
                ('hipunit', models.CharField(choices=[('cms', 'cms'), ('inches', 'inches')], max_length=20)),
                ('whratio', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('whratioderived', models.IntegerField(null=True)),
                ('foodhabits', models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Non-Vegetarian', 'Non-Vegetarian')], max_length=20, null=True)),
                ('uploaded_photo', models.ImageField(upload_to='AnemicLactatingMother/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='anemicadolescentgirl',
            fields=[
                ('uid', models.CharField(default=False, max_length=255, primary_key=True, serialize=False)),
                ('personalcontact', models.CharField(max_length=200)),
                ('ICDSname', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
