# Generated by Django 2.1.7 on 2019-03-18 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_date', models.DateField()),
                ('referred_by', models.CharField(blank=True, max_length=255)),
                ('date_incarcerated', models.DateField()),
                ('date_bail_set', models.DateField()),
                ('date_of_jail_interview', models.DateField()),
                ('charges', multiselectfield.db.fields.MultiSelectField(choices=[('ASSAULT / BATTERY', 'Assault / Battery'), ('BURGLARY', 'Burglary'), ('BRIBERY', 'Bribery'), ('DRUG POSSESSION', 'Drug Possession'), ('THEFT / LARCENY', 'Theft / Larceny')], max_length=66)),
                ('bail_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('facility', models.CharField(choices=[('CURRAN FROMHOLD CORRECTIONAL FACILITY', 'Curran-Fromhold Correctional Facility'), ('CORRECTIONS DEPARTMENT', 'Corrections Department'), ('JUVENILE JUSTICE SERVICES CENTER', 'Juvenile Justice Services Center'), ('PHILADELPHIA INDUSTRIAL CORRECTIONAL CENTER', 'Philadelphia Industrial Correctional Center')], max_length=255)),
                ('docket_number', models.IntegerField()),
                ('date_support_call_completed', models.DateField()),
                ('support_funding_source', models.CharField(blank=True, max_length=255)),
                ('opt_in_for_additional_resources', models.BooleanField(default=False)),
                ('attachment', models.FileField(blank=True, upload_to='documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=25)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pronoun', models.CharField(blank=True, choices=[('MR', 'Mr'), ('MRS', 'Mrs'), ('MS', 'Ms'), ('MISS', 'Miss')], max_length=4)),
                ('race', multiselectfield.db.fields.MultiSelectField(choices=[('AFRICAN AMERICAN', 'African American'), ('AMERICAN INDIAN', 'American Indian'), ('ASIAN', 'Asian'), ('HISPANIC OR LATINO', 'Hispanic or Latino'), ('NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER', 'Native Hawaiian or Other Pacific Islander'), ('WHITE', 'White')], max_length=105)),
                ('date_of_birth', models.DateField(blank=True)),
                ('open_to_speaking_to_the_press', models.BooleanField(default=False)),
                ('ok_with_being_photographed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=25)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='case',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client'),
        ),
        migrations.AddField(
            model_name='case',
            name='support_caller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
