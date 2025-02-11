from django.core.management.base import BaseCommand
from django.db import transaction
from food_service.models import FoodCategory, Food


class Command(BaseCommand):
    help = 'Fills database with test data for restaurant menu'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to fill test data...')

        Food.objects.all().delete()
        FoodCategory.objects.all().delete()

        drinks = FoodCategory.objects.create(
            name_ru='Напитки',
            name_en='Drinks',
            order_id=10
        )

        bakery = FoodCategory.objects.create(
            name_ru='Выпечка',
            name_en='Bakery',
            order_id=20
        )

        main_dishes = FoodCategory.objects.create(
            name_ru='Основные блюда',
            name_en='Main Dishes',
            order_id=30
        )

        tea = Food.objects.create(
            category=drinks,
            name_ru='Чай',
            description_ru='Чай 100 гр',
            internal_code=100,
            code=1,
            cost='123.00',
            is_publish=True
        )

        cola = Food.objects.create(
            category=drinks,
            name_ru='Кола',
            description_ru='Кола',
            internal_code=200,
            code=2,
            cost='123.00',
            is_publish=True
        )

        sprite = Food.objects.create(
            category=drinks,
            name_ru='Спрайт',
            description_ru='Спрайт',
            internal_code=300,
            code=3,
            cost='123.00',
            is_publish=True
        )

        baikal = Food.objects.create(
            category=drinks,
            name_ru='Байкал',
            description_ru='Байкал',
            internal_code=400,
            code=4,
            cost='123.00',
            is_publish=True
        )

        croissant = Food.objects.create(
            category=bakery,
            name_ru='Круассан',
            description_ru='Свежий круассан',
            internal_code=500,
            code=5,
            cost='150.00',
            is_publish=True
        )

        pie = Food.objects.create(
            category=bakery,
            name_ru='Пирожок',
            description_ru='Пирожок с яблоком',
            internal_code=600,
            code=6,
            cost='80.00',
            is_publish=True
        )

        steak = Food.objects.create(
            category=main_dishes,
            name_ru='Стейк',
            description_ru='Стейк из говядины',
            internal_code=700,
            code=7,
            cost='1500.00',
            is_publish=True,
            is_special=True
        )

        pasta = Food.objects.create(
            category=main_dishes,
            name_ru='Паста',
            description_ru='Паста Карбонара',
            internal_code=800,
            code=8,
            cost='650.00',
            is_publish=True
        )

        coffee = Food.objects.create(
            category=drinks,
            name_ru='Кофе',
            description_ru='Кофе Американо',
            internal_code=900,
            code=9,
            cost='200.00',
            is_publish=False
        )

        tea.additional.add(cola)
        steak.additional.add(cola, sprite)

        self.stdout.write(self.style.SUCCESS('Successfully filled test data'))