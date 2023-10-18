import os
from datetime import date

from django.http import FileResponse, HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import AnonRateThrottle
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.models import User, Files
from app.serializers import UserGetSerializer, UserCreateSerializer, FilesSerializer
from my_first_cloud.settings import MEDIA_ROOT


# https://django.fun/ru/docs/django-rest-framework/3.12/api-guide/viewsets/
# https://ilovedjango.com/django/rest-api-framework/views/tips/sub/modelviewset-django-rest-framework/
# https://www.cdrf.co/3.12/rest_framework.viewsets/ModelViewSet.html
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    throttle_classes = [AnonRateThrottle]


class UserGetView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = User.objects.filter(id=user_id)
        return queryset


class FilesItemUserView(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Files.objects.filter(user=user_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TestView(APIView):
    def get(self, request):
        return Response({'status': 'OK'})


class FilesDownloadView(APIView):
    def get(self, request, hash):
        try:
            data = Files.objects.filter(url_hash=hash)
            path = str(data[0].file)
        except:
            return HttpResponse('<h2>Не найдено</h2>')
        else:
            today = date.today()
            root = MEDIA_ROOT
            # Получаем путь к файлу
            file_path = str(root) + '/' + path
            # Проверяем, существует ли файл
            if os.path.exists(file_path):
                data.update(download_date=str(today))
                return FileResponse(open(file_path, 'rb'), as_attachment=True)
            return HttpResponse('<h2>Not found</h2>')
