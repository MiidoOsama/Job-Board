# Generated by Django 5.0.1 on 2024-02-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_bloglist_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('TECH', 'Technology'), ('SPORTS', 'Sports'), ('ENTERTAINMENT', 'Entertainment'), ('TRAVELLIFESTYLE', 'Travel,Lifestyle'), ('FOOD', 'Food & Tasty')], max_length=20),
        ),
    ]
