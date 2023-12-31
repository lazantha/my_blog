# Generated by Django 4.2.3 on 2023-09-20 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dp', models.FileField(null=True, upload_to='')),
                ('email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PostTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.usertable')),
            ],
        ),
    ]
