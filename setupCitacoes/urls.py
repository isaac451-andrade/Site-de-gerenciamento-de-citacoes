from django.contrib import admin
from django.urls import path, include
from paginaCitacoes.views import mainPage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginCadastro.urls')),
    path('main/', mainPage, name="mainPage")
]
