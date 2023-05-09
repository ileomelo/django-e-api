from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def recipe_v2_list(request):
    return Response("Recipe v2 list")
