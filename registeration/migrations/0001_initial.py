# Generated by Django 4.0.6 on 2022-09-17 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('other_name', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=20)),
                ('home_town', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=20)),
                ('previous_school_if_any', models.CharField(max_length=20)),
                ('father_Guardian_name', models.CharField(max_length=100)),
                ('contact_address', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('mother_phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('local_government', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registeration.lga')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registeration.section')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registeration.session')),
                ('state_of_origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registeration.state')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registeration.student_class')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registeration.term')),
            ],
        ),
    ]
