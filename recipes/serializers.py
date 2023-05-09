from rest_framework import serializers

from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ["preparation_steps_is_html", "cover", "is_published"]

