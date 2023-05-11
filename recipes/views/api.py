# flake8: noqa
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from tag.models import Tag

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer


class RecipeV2ListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.get_published()
        serializer = RecipeSerializer(recipes, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                author_id=1,
                category_id=1,
                tags=[1, 2],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeV2DetailView(APIView):
    def get_recipe(self, pk):
        recipe = get_object_or_404(Recipe.objects.get_published(), pk=pk)
        return recipe

    def get(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(recipe, many=False, context={"request": request})
        return Response(serializer.data)

    def patch(self, request, pk):
        recipe = self.get_recipe(pk)
        serializer = RecipeSerializer(
            recipe,
            data=request.data,
            partial=True,
            many=False,
            context={"request": request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = self.get_recipe(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# TAGS
@api_view()
def tag_api_v2_detail(request, pk):
    tag = get_object_or_404(Tag.objects.all(), pk=pk)
    serializer = TagSerializer(instance=tag, many=False, context={"request": request})
    return Response(serializer.data)
