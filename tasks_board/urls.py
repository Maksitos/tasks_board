"""tasks_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from tasks_board_app.API.resources import TaskViewSet, UserViewSet
from tasks_board_app.views import *
from tasks_board_app.consumers import InfoConsumer
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BoardPage.as_view(), name='board_page'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('registration', Registration.as_view(), name='register'),
    path('add_task', TaskCreationPage.as_view(),name='add_task'),
    path('status_change', StatusChangeView.as_view(), name='status_change'),
    path('<pk>/update', UpdateTask.as_view(), name='update'),
    path('<pk>/delete', DeleteTask.as_view(), name='delete'),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),



]
