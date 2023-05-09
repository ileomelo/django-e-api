from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Recipe
from ..serializers import RecipeSerializer


@api_view()
def recipe_v2_list(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True, context={"request": request})
    return Response(serializer.data)


@api_view()
def recipe_v2_detail(request, pk):
    recipe = get_object_or_404(Recipe.objects.get_published(), pk=pk)
    serializer = RecipeSerializer(recipe, context={"request": request})
    return Response(serializer.data)
