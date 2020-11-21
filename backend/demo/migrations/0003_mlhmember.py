# Generated by Django 3.1.3 on 2020-11-21 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20201121_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='MLHMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('member_url', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
