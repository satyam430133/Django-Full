from .serializers import FoodSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *

@api_view(['GET','POST'])
def Item_List(request):
    if request.method == 'GET':
        itemlist = FoodItemModel.objects.all()
        serializer = FoodSerializer(itemlist,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = FoodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: return Response(serializer.errors)
@api_view(['GET','PUT','DELETE'])
def Item(request,pk):
    if request.method == 'GET':
        try:
            item = FoodItemModel.objects.get(pk=pk)
        except FoodItemModel.DoesNotExist:
            return Response ({'error':'Details Not Found'},status=status.HTTP_404_NOT_FOUND)
        serializer = FoodSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        item = FoodItemModel.objects.get(pk=pk)
        serializer = FoodSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: return Response(serializer.errors)
    elif request.method == 'DELETE':
        item = FoodItemModel.objects.get(pk=pk)
        item.delete()
        return Response ({'error':"Data Deleted Successfully"})