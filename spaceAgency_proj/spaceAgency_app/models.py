from django.db import models
from filer.fields.image import FilerImageField
from adminsortable2.admin import SortableAdminMixin
from django.utils.translation import gettext_lazy as _

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
        verbose_name = _("Слайдер")
        verbose_name_plural = _("Слайдеры")
        ordering = ['my_order']

    def __str__(self):
        return self.title
