from rest_framework import viewsets, permissions
from django.http import HttpResponse
from .models import User, Siswa, Guru, Jadwal, Tugas, TugasSiswa, Dokumentasi, ProgressPKL, Kelas, Jurusan
from .serializers import *

class BaseViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']  # PATCH dihapus

class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class SiswaViewSet(BaseViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer
    permission_classes = [permissions.AllowAny]

class GuruViewSet(BaseViewSet):
    queryset = Guru.objects.all()
    serializer_class = GuruSerializer
    permission_classes = [permissions.AllowAny]

class JadwalViewSet(BaseViewSet):
    queryset = Jadwal.objects.all()
    serializer_class = JadwalSerializer
    permission_classes = [permissions.AllowAny]

class TugasViewSet(BaseViewSet):
    queryset = Tugas.objects.all()
    serializer_class = TugasSerializer
    permission_classes = [permissions.AllowAny]

class TugasSiswaViewSet(BaseViewSet):
    queryset = TugasSiswa.objects.all()
    serializer_class = TugasSiswaSerializer
    permission_classes = [permissions.AllowAny]

class DokumentasiViewSet(BaseViewSet):
    queryset = Dokumentasi.objects.all()
    serializer_class = DokumentasiSerializer
    permission_classes = [permissions.AllowAny]

class ProgressViewSet(BaseViewSet):
    queryset = ProgressPKL.objects.all()
    serializer_class = ProgressSerializer
    permission_classes = [permissions.AllowAny]

class KelasViewSet(BaseViewSet):
    queryset = Kelas.objects.all()
    serializer_class = KelasSerializer
    permission_classes = [permissions.AllowAny]

class JurusanViewSet(BaseViewSet):
    queryset = Jurusan.objects.all()
    serializer_class = JurusanSerializer
    permission_classes = [permissions.AllowAny]

class ProgressPKLViewSet(BaseViewSet):
    queryset = ProgressPKL.objects.all().order_by('-id')
    serializer_class = ProgressPKLSerializer
    permission_classes = [permissions.IsAuthenticated]

def home(request):
    return HttpResponse("<h1>Selamat datang di Sistem Informasi UKK/PKL Online</h1>")