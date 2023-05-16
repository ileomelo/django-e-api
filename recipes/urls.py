from django.urls import path

from recipes import views
from recipes.views.api import RecipeAPIv2ViewSet

app_name = "recipes"

urlpatterns = [
    path("", views.RecipeListViewHome.as_view(), name="home"),
    path("recipes/search/", views.RecipeListViewSearch.as_view(), name="search"),
    path("recipes/tags/<slug:slug>/", views.RecipeListViewTag.as_view(), name="tag"),
    path(
        "recipes/category/<int:category_id>/",
        views.RecipeListViewCategory.as_view(),
        name="category",
    ),
    path("recipes/<int:pk>/", views.RecipeDetail.as_view(), name="recipe"),
    path(
        "recipes/api/v1/",
        views.RecipeListViewHomeApi.as_view(),
        name="recipes_api_v1",
    ),
    path(
        "recipes/api/v1/<int:pk>/",
        views.RecipeDetailAPI.as_view(),
        name="recipes_api_v1_detail",
    ),
    path(
        "recipes/theory/",
        views.theory,
        name="theory",
    ),
    path(
        "api/v2/",
        RecipeAPIv2ViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="recipe_v2_list",
    ),
    path(
        "api/v2/<int:pk>/",
        RecipeAPIv2ViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="recipe_v2_detail",
    ),
    path("api/v2/tag/<int:pk>/", views.tag_api_v2_detail, name="tag_api_v2_detail"),
]
