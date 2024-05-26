from django.contrib import admin
from .models import Slider
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer

@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{get_thumbnailer(obj.image)["admin_preview"].url}" />')
        else:
            return ''
    image_tag.allow_tags = True
    image_tag.short_description = 'Изображение'