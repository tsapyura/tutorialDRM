from django.contrib.auth.models import User, Group
from rest_framework import serializers

from quickstart.models import Product, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'user', 'description', 'approved_by', 'approved', 'display_on_main_page', 'categories']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'user']
