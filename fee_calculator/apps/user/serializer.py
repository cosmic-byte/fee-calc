from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )

    def create(self, validated_data):
        user = User.objects.create_base_user(
            email=validated_data.pop("email"),
            password=validated_data.pop("password"),
            **validated_data
        )
        return user


class UserRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ("email", "uid", "groups", "is_active")
        read_only_fields = ("groups",)


class UserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("email", "uid")


class EnableDisableUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def update(self, instance, validated_data, **kwargs):
        instance.is_active = not instance.is_active
        instance.save()
        return instance


class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def update(self, instance, validated_data, **kwargs):
        instance.deleted = not instance.deleted
        instance.save()
        return instance
