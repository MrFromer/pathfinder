# Generated by Django 3.2.6 on 2022-05-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_alter_character_character_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
