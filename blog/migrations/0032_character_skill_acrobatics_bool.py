# Generated by Django 3.2.6 on 2022-04-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20220421_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='skill_acrobatics_bool',
            field=models.BooleanField(null=True),
        ),
    ]
