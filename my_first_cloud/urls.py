"""
URL configuration for my_first_cloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import UserCreateView, UserGetView, FilesItemUserView, TestView, FilesDownloadView, UsersAdminView, \
    ItemUserFilesAdminView, TokenInView, TokenOutView, index
from my_first_cloud import settings

router = routers.DefaultRouter()
router.register('data', FilesItemUserView)
router.register('users', UsersAdminView)
router.register('content', ItemUserFilesAdminView)

urlpatterns = [
    path("", index, name="index"),
    path('staff/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/item/', include(router.urls)),
    path('reg/', UserCreateView.as_view()),
    path('user/', UserGetView.as_view()),
    path('auth/login/', TokenInView.as_view()),
    path('auth/logout/', TokenOutView.as_view()),
    path('test', TestView.as_view()),
    path('download/<hash>/', FilesDownloadView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
