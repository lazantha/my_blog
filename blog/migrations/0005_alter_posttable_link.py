# Generated by Django 4.2.3 on 2023-09-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_posttable_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttable',
            name='link',
            field=models.CharField(max_length=350),
        ),
    ]
