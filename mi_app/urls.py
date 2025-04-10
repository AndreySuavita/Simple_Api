from django.urls import path
from .views import MiModeloListView, MiModeloCreateView, MiModeloDeleteView, MiModeloUpdateView

urlpatterns = [
    path('api/mimodelo_get/', MiModeloListView.as_view(), name='mimodelo-list'),
    path('api/mimodelo_post/', MiModeloCreateView.as_view(), name='mimodelo-create'),
    path('api/mimodelo_delete/<int:pk>/', MiModeloDeleteView.as_view(), name='mimodelo-delete'),
    path('api/mimodelo_put_patch/<int:pk>/', MiModeloUpdateView.as_view(), name='mimodelo-update'),
]