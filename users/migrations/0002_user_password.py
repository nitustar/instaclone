# Generated by Django 5.0 on 2024-01-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='Scaler@123', max_length=55),
            preserve_default=False,
        ),
    ]
