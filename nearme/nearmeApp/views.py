from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializers import MemberSerializer

class ProductList(APIView):
    def get(self, request):
        products = Member.objects.all()
        serializer =MemberSerializer(products, many=True)
        return Response(serializer.data)
