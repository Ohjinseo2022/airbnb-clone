from django.shortcuts import render
from .models import Category

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# 위코드가 밑에코드들을 전부 대체해줌

# APIView
# class Categories(APIView):
#     def get(self, request):
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             new_category = serializer.save()
#             return Response(
#                 CategorySerializer(new_category).data,
#             )
#         else:
#             return Response(serializer.errors)


# 예전 방식
# @api_view(["GET", "POST"])
# def categories(request):
#     if request.method == "GET":
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         # print(request.data)
#         # Category.objects.create(
#         #     name=request.data["name"],
#         #     kind=request.data["kind"],
#         # )
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             new_category = serializer.save()
#             return Response(CategorySerializer(new_category).data)
#         else:
#             return Response(serializer.errors)

# APIView
# class CategoryDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise NotFound

#     def get(self, request, pk):
#         serialilzer = CategorySerializer(self.get_object(pk))
#         return Response(serialilzer.data)

#     def put(self, request, pk):
#         serialilzer = CategorySerializer(
#             self.get_object(pk),
#             data=request.data,
#             partial=True,
#         )
#         if serialilzer.is_valid():
#             updated_category = serialilzer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serialilzer.errors)

#     def delete(self, request, pk):
#         self.get_object(pk).delete()
#         return Response(status=HTTP_204_NO_CONTENT)


# @api_view(["GET", "PUT", "DELETE"])
# def category(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         raise NotFound
#     if request.method == "GET":
#         serialilzer = CategorySerializer(category)
#         return Response(serialilzer.data)
#     elif request.method == "PUT":
#         serialilzer = CategorySerializer(
#             category,
#             data=request.data,
#             partial=True,
#         )
#         if serialilzer.is_valid():
#             updated_category = serialilzer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serialilzer.errors)
#     elif request.method == "DELETE":
#         category.delete()
#         return Response(status=HTTP_204_NO_CONTENT)
