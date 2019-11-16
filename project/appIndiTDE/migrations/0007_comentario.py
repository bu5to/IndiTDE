# Generated by Django 2.2.6 on 2019-11-16 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appIndiTDE', '0006_sugerencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('texto', models.CharField(max_length=240)),
                ('ropa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appIndiTDE.Ropa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appIndiTDE.Usuario')),
            ],
        ),
    ]