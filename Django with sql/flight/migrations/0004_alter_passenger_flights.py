# Generated by Django 5.0.4 on 2024-05-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flight.flight'),
        ),
    ]
