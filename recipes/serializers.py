from rest_framework import serializers

from authors.validator import AuthorRecipeValidator
from recipes.models import Recipe

from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]


class RecipeSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if self.instance is not None and attrs.get("servings") is None:
            attrs["servings"] = self.instance.servings

        if self.instance is not None and attrs.get("preparation_time") is None:
            attrs["preparation_time"] = self.instance.preparation_time

        AuthorRecipeValidator(
            data=attrs,
            ErrorClass=serializers.ValidationError,
        )
        return super().validate(attrs)

    category = serializers.StringRelatedField(
        read_only=True,
    )
    tag_objects = TagSerializer(
        many=True,
        source="tags",
        read_only=True,
    )

    tag_links = serializers.HyperlinkedRelatedField(
        view_name="recipes:tag_api_v2_detail",
        read_only=True,
    )

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "author",
            "category",
            "tags",
            "tag_objects",
            "tag_links",
            "preparation_time",
            "preparation_time_unit",
            "servings",
            "servings_unit",
            "preparation_steps",
            "cover",
        ]
