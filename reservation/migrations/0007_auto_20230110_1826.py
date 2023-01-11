# Generated by Django 3.2.16 on 2023-01-10 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0006_alter_table_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='user',
        ),
        migrations.AddField(
            model_name='table',
            name='booker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booker', to=settings.AUTH_USER_MODEL),
        ),
    ]
