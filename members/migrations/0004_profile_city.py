# Generated by Django 5.1.4 on 2024-12-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_profile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
