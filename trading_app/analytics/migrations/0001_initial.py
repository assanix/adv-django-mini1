# Generated by Django 5.1.6 on 2025-02-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=255)),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField()),
            ],
        ),
    ]
