from rest_framework.decorators import api_view
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework.response import Response

@api_view(['GET'])
def recipes_list(request):
    data = Recipe.objects.all()
    serializer = RecipeSerializer(data, many=True)
    return Response(serializer.data)

