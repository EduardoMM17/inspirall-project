from rest_framework.views import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def call_simplefact(request):
    person = {'name': 'Dennis', 'age': 28}
    return Response(person)