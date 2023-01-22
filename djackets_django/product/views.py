from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework .decorators import api_view
from .models import Product, Category, FavoriteProduct, Profile
from django.http import Http404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages

# change = Change.objects.get(id=request.POST.get('change_id'))
# change.endtime = datetime.now()
# change.save()


@api_view(['POST'])
def updateprof(request):
    new_profile = Profile.objects.filter(
        name=request.data['username']).get(name=request.data['username'])
    new_profile.name = request.data['name']
    new_profile.profileimg = request.data['file']
    new_profile.save()
    serializer = ProfileSerializer(new_profile)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    my_profile = Profile.objects.filter(
        name=request.data['username']).get(name=request.data['username'])
    print(my_profile.profileimg)
    serializer = ProfileSerializer(my_profile)
    print(serializer.data)
    return Response(serializer.data)

# class FavoriteProductsList(APIView):
#     def get(self, request, format=None):
#         print(request.user)
#         products = Product.objects.filter(
#             Q(user=request.user) )
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)


@api_view(['POST'])
def signup(request):
    print(request.data)

    user = User.objects.create_user(
        username=request.data["username"], password=request.data["password"])
    user.save()

    user_model = User.objects.get(username=request.data["username"])
    new_profile = Profile.objects.create(
        user=user_model, id_user=user_model.id, profileimg=request.data["file"], name=request.data["username"])
    new_profile.save()
    serializer = ProfileSerializer(new_profile)
    print(serializer.data)
    return Response(serializer.data)


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(Category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
