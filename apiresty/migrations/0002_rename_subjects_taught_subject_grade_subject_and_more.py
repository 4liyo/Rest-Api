# Generated by Django 5.0.2 on 2024-02-10 08:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiresty', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='subjects_taught',
            new_name='Subject',
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='apiresty.subject'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
