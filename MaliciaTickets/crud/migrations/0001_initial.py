# Generated by Django 4.2.2 on 2023-06-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('lugar', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('entradas_disponibles', models.IntegerField()),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(null=True, upload_to='eventos')),
            ],
        ),
    ]
