from dataclasses import fields
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset = User.objects.all())])

    password = serializers.CharField(write_only =True,required=True, validators=[validate_password], style ={'input_type': 'password'})

    confirm_password = serializers.CharField(write_only=True, required=True, style ={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','email', 'password', 'confirm_password', 'phone', 'country', 'business_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':{"Password fields didn't match"}})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone = validated_data['phone'],
            country = validated_data['country'],
            business_name = validated_data['business_name'],
            )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields= ['email', 'password']

# send invite mail
class InviteUserViaEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset = User.objects.all())])

    class Meta:
        model = User
        fields = ['email']


class RegisterInviteUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset = User.objects.all())])

    password = serializers.CharField(write_only =True,required=True, validators=[validate_password], style ={'input_type': 'password'})

    confirm_password = serializers.CharField(write_only=True, required=True, style ={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','email', 'password', 'confirm_password', 'phone')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':{"Password fields didn't match"}})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone = validated_data['phone'],
            )

        user.set_password(validated_data['password'])
        user.save()

        return user


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'


class PurchaseMemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseMemo
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"