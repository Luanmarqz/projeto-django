from django.urls import path
from core import views


app_name = 'core'

urlpatterns = [
    path('', views.OcorrenciaView.as_view(), name='list'),
    path('create/', views.OcorrenciaCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.OcorrenciaUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.OcorrenciaDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.OcorrenciaDeleteView.as_view(), name='delete'),
]
