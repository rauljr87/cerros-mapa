# Generated by Django 4.0.4 on 2022-06-29 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Latitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degrees', models.IntegerField(verbose_name='Grados')),
                ('minutes', models.IntegerField(verbose_name='Minutes')),
                ('seconds', models.IntegerField(verbose_name='Seconds')),
                ('direction', models.CharField(choices=[('0', 'N'), ('1', 'S')], max_length=10, verbose_name='Directions')),
            ],
        ),
        migrations.CreateModel(
            name='Longitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degrees', models.IntegerField(verbose_name='Grados')),
                ('minutes', models.IntegerField(verbose_name='Minutes')),
                ('seconds', models.IntegerField(verbose_name='Seconds')),
                ('direction', models.CharField(choices=[('0', 'E'), ('1', 'W')], max_length=10, verbose_name='Directions')),
            ],
        ),
        migrations.CreateModel(
            name='Cerro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del Cerro')),
                ('latitud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cerro.latitud')),
                ('longitud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cerro.longitud')),
            ],
        ),
    ]
