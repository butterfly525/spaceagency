from django.db import models
from filer.fields.image import FilerImageField
from adminsortable2.admin import SortableAdminMixin


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название слайдера')
    image = FilerImageField(on_delete=models.CASCADE,
                            verbose_name='Изображение')
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False, verbose_name='Сортировка'
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return self.title
