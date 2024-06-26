# Generated by Django 5.0.6 on 2024-05-29 11:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0005_alter_sings_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='sings',
            name='difficult',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='guitar.difficulty'),
        ),
    ]
