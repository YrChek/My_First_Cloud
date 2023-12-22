import logging
import os
from datetime import date

from django.http import FileResponse, HttpResponse
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.throttling import AnonRateThrottle
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

logger = logging.getLogger(__name__)
# logger = logging.getLogger('app')

from app.models import User, Files
from app.paginator import UserAPIListPagination
from app.serializers import UserGetSerializer, UserCreateSerializer, FilesSerializer, UserAdminSerializer, \
    FilesAdminSerializer
from my_first_cloud.settings import MEDIA_ROOT


def index(request):
    return render(request, "build/index.html")


class TokenInView(TokenCreateView):
    def post(self, request, **kwargs):
        logger.debug('Запрос на получение токена')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = super()._action(serializer)
        logger.debug('%s %s %s' % ('Пользователь', request.data['username'], 'вошел в систему'))
        return response


class TokenOutView(TokenDestroyView):
    def post(self, request):
        logger.debug('Запрос выхода из системы')
        response = super().post(request)
        logger.debug('%s %s %s' % ('Пользователь', self.request.user, 'вышел из системы'))
        return response


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    throttle_classes = [AnonRateThrottle]

    def create(self, request, *args, **kwargs):
        logger.debug('UserCreateView request: %s %s' % (request.method, request.path))
        response = super().create(request, *args, **kwargs)
        logger.debug('UserCreateView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response


class UserGetView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = User.objects.filter(id=user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        logger.debug('UserGetView request: %s %s' % (request.method, request.path))
        response = super().list(request, *args, **kwargs)
        logger.debug('UserGetView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response


class FilesItemUserView(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Files.objects.filter(user=user_id)
        return queryset

    def list(self, request, *args, **kwargs):
        logger.debug('FilesItemUserView: %s %s' % (request.method, request.path))
        response = super().list(request, *args, **kwargs)
        logger.debug('FilesItemUserView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response

    def create(self, request, *args, **kwargs):
        logger.debug('FilesItemUserView: %s %s' % (request.method, request.path))
        response = super().create(request, *args, **kwargs)
        logger.debug('FilesItemUserView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        logger.debug('FilesItemUserView: %s %s' % (request.method, request.path))
        response = super().retrieve(request, *args, **kwargs)
        logger.debug('FilesItemUserView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response

    def update(self, request, *args, **kwargs):
        logger.debug('FilesItemUserView: %s %s' % (request.method, request.path))
        response = super().update(request, *args, **kwargs)
        logger.debug('FilesItemUserView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response

    def destroy(self, request, *args, **kwargs):
        logger.debug('FilesItemUserView: %s %s' % (request.method, request.path))
        response = super().destroy(request, *args, **kwargs)
        logger.debug('FilesItemUserView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response


class UsersAdminView(ModelViewSet):
    queryset = User.objects.exclude(is_superuser=True)
    serializer_class = UserAdminSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = UserAPIListPagination

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(method='POST')

    def list(self, request, *args, **kwargs):
        logger.debug('UsersAdminView: %s %s' % (request.method, request.path))
        response = super().list(request, *args, **kwargs)
        logger.debug('UsersAdminView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response

    def update(self, request, *args, **kwargs):
        logger.debug('UsersAdminView: %s %s' % (request.method, request.path))
        response = super().update(request, *args, **kwargs)
        logger.debug('UsersAdminView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response

    def destroy(self, request, *args, **kwargs):
        logger.debug('UsersAdminView: %s %s' % (request.method, request.path))
        response = super().destroy(request, *args, **kwargs)
        logger.debug('UsersAdminView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response


class ItemUserFilesAdminView(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesAdminSerializer
    permission_classes = (IsAdminUser,)

    def list(self, request, *args, **kwargs):
        logger.debug('ItemUserFilesAdminView: %s %s' % (request.method, request.path))
        user = request.query_params.get('user')
        if user:
            query_set = Files.objects.filter(user=user)
        else:
            query_set = Files.objects.all()
        response = Response(self.serializer_class(query_set, many=True).data, status=status.HTTP_200_OK)
        logger.debug('ItemUserFilesAdminView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed(method='POST')

    def destroy(self, request, *args, **kwargs):
        logger.debug('ItemUserFilesAdminView: %s %s' % (request.method, request.path))
        response = super().destroy(request, *args, **kwargs)
        logger.debug('ItemUserFilesAdminView: method %s %s %s %s' %
                     (request.method, 'response', '->', 'status: %s' % (response.status_code)))
        return response


class TestView(APIView):
    def get(self, request):
        return Response({'status': 'OK'})


class FilesDownloadView(APIView):
    def get(self, request, hash):
        logger.debug('FilesDownloadView: %s %s' % (request.method, request.path))
        try:
            data = Files.objects.filter(url_hash=hash)
            path = str(data[0].file)
        except:
            logger.debug('FilesDownloadView: объект не найден')
            return HttpResponse('<h2>Не найдено</h2>')
        else:
            today = date.today()
            root = MEDIA_ROOT
            # Получаем путь к файлу
            file_path = str(root) + '/' + path
            # Проверяем, существует ли файл
            if os.path.exists(file_path):
                data.update(download_date=str(today))
                logger.debug('FilesDownloadView: файл загружается')
                return FileResponse(open(file_path, 'rb'), as_attachment=True)
            logger.debug('FilesDownloadView: файл не найден')
            return HttpResponse('<h2>Not found</h2>')
