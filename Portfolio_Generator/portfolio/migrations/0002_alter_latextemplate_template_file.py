# Generated by Django 5.1.7 on 2025-03-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latextemplate',
            name='template_file',
            field=models.TextField(blank=True),
        ),
    ]
