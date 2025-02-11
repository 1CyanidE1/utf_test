from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Exists, OuterRef, Prefetch
from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodListView(APIView):
    def get(self, request):
        published_foods = Prefetch(
            'food',
            queryset=Food.objects.filter(is_publish=True)
        )

        has_published_foods = Food.objects.filter(
            category=OuterRef('pk'),
            is_publish=True
        )

        categories = FoodCategory.objects.annotate(
            has_foods=Exists(has_published_foods)
        ).filter(
            has_foods=True
        ).prefetch_related(published_foods)

        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)

