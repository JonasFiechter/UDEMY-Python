from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.ver_contato, name='contato_ver_contato'),
    path('busca/', views.busca, name='busca')
]
