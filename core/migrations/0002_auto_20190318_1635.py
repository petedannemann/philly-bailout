# Generated by Django 2.1.7 on 2019-03-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='facility',
            field=models.CharField(choices=[('CURRAN FROMHOLD CORRECTIONAL FACILITY', 'Curran-Fromhold Correctional Facility'), ('CORRECTIONS DEPARTMENT', 'Corrections Department'), ('JUVENILE JUSTICE SERVICES CENTER', 'Juvenile Justice Services Center'), ('PHILADELPHIA INDUSTRIAL CORRECTIONAL CENTER', 'Philadelphia Industrial Correctional Center')], max_length=255),
        ),
    ]
