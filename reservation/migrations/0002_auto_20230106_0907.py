# Generated by Django 3.2.16 on 2023-01-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]