# Generated by Django 4.0.6 on 2022-09-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0006_alter_student_other_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='is_current',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='term',
            name='is_current',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]