# Generated by Django 5.0.6 on 2024-07-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0005_chordsgroup_group_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chords',
            name='designation',
            field=models.CharField(db_index=True, default=None, max_length=100, null=True, verbose_name='Обозначение'),
        ),
    ]
