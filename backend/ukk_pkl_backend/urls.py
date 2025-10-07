"""
URL configuration for ukk_pkl_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import routers
from core.views import *
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import JadwalViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'siswa', SiswaViewSet)
router.register(r'guru', GuruViewSet)
router.register(r'jadwal', JadwalViewSet)
router.register(r'tugas', TugasViewSet)
router.register(r'tugas-siswa', TugasSiswaViewSet)
router.register(r'dokumentasi', DokumentasiViewSet)
router.register(r'progress', ProgressViewSet)
router.register(r'kelas', KelasViewSet)
router.register(r'jurusan', JurusanViewSet)


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),  # login bawaan DRF
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

def home(request):
    return JsonResponse({"message": "Sistem Informasi UKK/PKL API Ready"})