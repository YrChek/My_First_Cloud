import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from app.models import User, Files


class UserCreateSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=254, allow_blank=True)
    full_name = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'full_name']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            relative_path=f'/{validated_data["username"]}'
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserGetSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'is_staff']
        read_only_fields = ['username', 'is_staff']


class UserDelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['id', 'comment', 'file', 'filename', 'create_at', 'download_date', 'size', 'type', 'url_hash']
        read_only_fields = ['id', 'create_at', 'url_hash']

    def validate(self, attrs):
        user = self.context["request"].user
        method = self.context["request"].method
        if method == 'POST':
            try:
                user_name = str(user)
                filename = attrs['filename']
                re_filename = re.sub(' ', '_', filename)
                file = f'{user_name}/{re_filename}'
                obj = Files.objects.get(user=user, file=file)
                file_name = obj.filename
            except:
                return attrs
            else:
                raise ValidationError(f'Этот файл уже существует под названием {file_name}')
        return attrs


class UserAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'is_staff', 'email','files']
        read_only_fields = ['id', 'username', 'full_name', 'files']


class FilesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['id','filename', 'type', 'comment', 'create_at', 'size']
        read_only_fields = ['id', 'create_at']
