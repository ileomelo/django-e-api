# flake8: noqa
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tag.models import Tag

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer


class MyPaginationView(PageNumberPagination):
    page_size = 5


class RecipeAPIv2ViewSet(ModelViewSet):
    # QuerySet
    queryset = Recipe.objects.get_published()
    # Serializer
    serializer_class = RecipeSerializer
    pagination_class = MyPaginationView


# TAGS
@api_view()
def tag_api_v2_detail(request, pk):
    tag = get_object_or_404(Tag.objects.all(), pk=pk)
    serializer = TagSerializer(instance=tag, many=False, context={"request": request})
    return Response(serializer.data)
