# Generated by Django 4.2.3 on 2023-09-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_posttable_category_alter_posttable_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttable',
            name='category',
            field=models.CharField(max_length=25),
        ),
    ]
