# Generated by Django 4.2.13 on 2024-06-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_alter_user_gender_volunteer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
