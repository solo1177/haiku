# Generated by Django 2.2.1 on 2020-01-30 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_remove_register_haiku_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='haiku_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
