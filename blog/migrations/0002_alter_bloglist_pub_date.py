# Generated by Django 5.0.1 on 2024-02-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglist',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
