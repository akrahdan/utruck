# Generated by Django 3.2.9 on 2021-11-28 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('riders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('source_lat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('source_lng', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('dest_lat', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('dest_lng', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riders.rider')),
            ],
        ),
    ]
