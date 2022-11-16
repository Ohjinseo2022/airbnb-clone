from django.shortcuts import render
from .models import Category

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import CategorySerializer

# Create your views here.
@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # print(request.data)
        # Category.objects.create(
        #     name=request.data["name"],
        #     kind=request.data["kind"],
        # )
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound
    if request.method == "GET":
        serialilzer = CategorySerializer(category)
        return Response(serialilzer.data)
    elif request.method == "PUT":
        serialilzer = CategorySerializer(
            category,
            data=request.data,
            partial=True,
        )
        if serialilzer.is_valid():
            updated_category = serialilzer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serialilzer.errors)
