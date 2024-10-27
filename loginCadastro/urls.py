from django.urls import path
from .views import *
urlpatterns = [
    path('', loginView, name='loginPage'),
    path('cadastro/', cadastroView, name='cadastroPage')

]