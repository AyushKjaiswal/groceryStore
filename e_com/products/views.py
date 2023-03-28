from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
# Create your views here.

# class ProductView(APIView):
#     def get(self,request):
#         queryset = Products.objects.all()
#         serializer = ProductSeriallizers(queryset,many =True)
#         return Response(serializer.data)

class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({'success':'user is authenticated'})



class ProductView(APIView):
    def get(self,request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Products.objects.filter(category__category_name=category)
        else:
            queryset = Products.objects.all()
        serializer = ProductSeriallizers(queryset,many =True)
        return Response({'count': len(serializer.data),'data' :serializer.data})
    

    