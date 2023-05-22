# flake8: noqa
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tag.models import Tag

from ..models import Recipe
from ..permissions import IsOwnerOrReadOnly
from ..serializers import RecipeSerializer, TagSerializer


class MyPaginationView(PageNumberPagination):
    page_size = 5


class RecipeAPIv2ViewSet(ModelViewSet):
    # Métodos permitidos //  OBS: OS MÉTODOS PRECISAM ESTAR EM LETRA MINÚSCULAS
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    # QuerySet
    queryset = Recipe.objects.get_published()

    # Serializer
    serializer_class = RecipeSerializer
    pagination_class = MyPaginationView
    permission_classes = [
        IsOwnerOrReadOnly,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


# TAGS
@api_view()
def tag_api_v2_detail(request, pk):
    tag = get_object_or_404(Tag.objects.all(), pk=pk)
    serializer = TagSerializer(instance=tag, many=False, context={"request": request})
    return Response(serializer.data)
