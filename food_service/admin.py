from django.contrib import admin
from .models import FoodCategory, Food


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'name_en', 'name_ch', 'order_id']
    list_editable = ['order_id']
    search_fields = ['name_ru', 'name_en', 'name_ch']
    ordering = ['order_id', 'name_ru']


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        'name_ru',
        'category',
        'internal_code',
        'code',
        'cost',
        'is_vegan',
        'is_special',
        'is_publish'
    ]
    list_filter = [
        'category',
        'is_vegan',
        'is_special',
        'is_publish'
    ]
    search_fields = [
        'name_ru',
        'description_ru',
        'internal_code',
        'code'
    ]
    list_editable = [
        'cost',
        'is_vegan',
        'is_special',
        'is_publish'
    ]
    filter_horizontal = ['additional']
    raw_id_fields = ['category']
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'category',
                'internal_code',
                'code',
                'cost',
            )
        }),
        ('Названия и описания', {
            'fields': (
                'name_ru',
                'description_ru',
                'description_en',
                'description_ch',
            )
        }),
        ('Дополнительные характеристики', {
            'fields': (
                'is_vegan',
                'is_special',
                'is_publish',
                'additional',
            )
        }),
    )