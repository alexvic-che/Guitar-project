# Generated by Django 5.0.6 on 2024-05-31 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0009_authors_alter_chords_slug_sings_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chords',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
