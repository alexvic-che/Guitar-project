# Generated by Django 5.0.6 on 2024-07-02 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar', '0010_alter_chords_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name': 'Автор песни', 'verbose_name_plural': 'Авторы песен'},
        ),
        migrations.AlterModelOptions(
            name='difficulty',
            options={'verbose_name': 'Сложность песни', 'verbose_name_plural': 'Сложность песен'},
        ),
        migrations.AlterModelOptions(
            name='sings',
            options={'ordering': ['-time_create'], 'verbose_name': 'Песня', 'verbose_name_plural': 'Песни'},
        ),
        migrations.AddField(
            model_name='sings',
            name='card_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='card_images', verbose_name='Картинка карточки'),
        ),
        migrations.AlterField(
            model_name='authors',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='chords',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Аккорды'),
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Сложность'),
        ),
        migrations.AlterField(
            model_name='sings',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sings', to='guitar.authors', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='sings',
            name='difficult',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sings', to='guitar.difficulty', verbose_name='Сложность'),
        ),
        migrations.AlterField(
            model_name='sings',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='sings',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='sings',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название песни'),
        ),
    ]