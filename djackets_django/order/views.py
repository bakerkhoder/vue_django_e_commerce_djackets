import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])
def checkout(request):
    print("fetna")
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        print(serializer.is_valid())
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get(
            'quantity') * item.get('product').price for item in serializer.validated_data['items'])
        print(serializer.validated_data)
        print(request.user)
        print(paid_amount)
        try:

            # charge = stripe.Charge.create(
            #     amount=int(paid_amount * 100),
            #     currency='USD',
            #     description='Charge from Djackets',
            #     source=serializer.validated_data['stripe_token']
            # )
            print(request.user)
            new_order = Order.objects.create(
                user=request.user,
                first_name=serializer.data['first_name'],
                last_name=serializer.data['last_name'],
                email=serializer.data['email'],
                address=serializer.data['address'],
                zipcode=serializer.data['zipcode'],
                place=serializer.data['place'],
                phone=serializer.data['phone'],
                paid_amount=paid_amount,
                stripe_token=serializer.data['stripe_token'],
            )
            items_data = serializer.validated_data.pop('items')
            print(items_data)
            for item_data in items_data:
                OrderItem.objects.create(order=new_order, **item_data)

            print("lahon meshi")
            print(serializer)
            # serializer.save(user=request.user, paid_amount=paid_amount)
            print("lahon meshi")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)
