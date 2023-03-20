# Generated by Django 2.2.5 on 2023-01-28 08:13

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(blank=True, max_length=100)),
                ('activity_type', models.CharField(blank=True, choices=[('Dining', 'Dining'), ('Attractions', 'Attractions'), ('Travel', 'Travel')], default='', max_length=100)),
                ('budget_type', models.CharField(blank=True, choices=[('$', 'Cheap'), ('$$', 'Average'), ('$$$', 'Expensive')], default='', max_length=100)),
                ('credit_for_submission', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=3)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('temperature', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=60)),
                ('last_name', models.CharField(blank=True, default='', max_length=60)),
                ('email', models.CharField(blank=True, default='', max_length=60)),
                ('user_name', models.CharField(blank=True, default='', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='VegasTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('VegasTemps', django.db.models.manager.Manager()),
            ],
        ),
    ]
