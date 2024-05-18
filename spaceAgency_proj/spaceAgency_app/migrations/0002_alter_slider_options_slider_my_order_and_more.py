# Generated by Django 4.2.13 on 2024-05-18 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('spaceAgency_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='slider',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название слайдера'),
        ),
    ]
