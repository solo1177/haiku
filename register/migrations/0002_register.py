# Generated by Django 2.1.2 on 2019-01-11 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kamigo', models.CharField(max_length=5)),
                ('nakasiti', models.CharField(max_length=7)),
                ('simogo', models.CharField(max_length=5)),
                ('posted_at', models.DateTimeField(verbose_name='date published')),
                ('like', models.IntegerField(default=0)),
            ],
        ),
    ]
