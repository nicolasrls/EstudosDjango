# Generated by Django 5.0.6 on 2024-06-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='dt_criacao',
            field=models.DateTimeField(auto_now_add=True, default='2024-06-18 15:56'),
            preserve_default=False,
        ),
    ]