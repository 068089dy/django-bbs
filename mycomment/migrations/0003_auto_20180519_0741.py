# Generated by Django 2.0.4 on 2018-05-19 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycomment', '0002_auto_20180518_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='father_id',
            new_name='father',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
