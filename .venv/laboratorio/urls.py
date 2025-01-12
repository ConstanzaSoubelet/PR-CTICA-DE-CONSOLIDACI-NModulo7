from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.LaboratorioList.as_view(), name='laboratorio_list'),
    path('nuevo/', views.LaboratorioCreate.as_view(), name='laboratorio_create'),
    path('<int:pk>/editar/', views.LaboratorioUpdate.as_view(), name='laboratorio_update'),
    path('<int:pk>/eliminar/', views.LaboratorioDelete.as_view(), name='laboratorio_delete'),
    path('<int:pk>/', views.LaboratorioDetail.as_view(), name='laboratorio_detail'),
]
