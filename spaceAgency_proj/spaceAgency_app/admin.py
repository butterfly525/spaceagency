from django.contrib import admin
from .models import Slider
from django.utils.safestring import mark_safe
# from django_admin_sortable2.admin import sortable2_admin_register
from adminsortable2.admin import SortableAdminMixin


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="width:50%;height:50%;object-fit:cover;"/>')
        else:
            return ''
    image_tag.allow_tags = True
    image_tag.short_description = 'Изображение'