# Generated by Django 4.1.4 on 2023-06-05 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phase1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]