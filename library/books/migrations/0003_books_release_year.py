# Generated by Django 5.0.6 on 2024-06-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_image_books_pages_ofbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='release_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
