from django.urls import path
from .views import contactView, successView, ProjectDetailView, ProjectCreateView, ProjectDeleteView, ProjectUpdateView

urlpatterns = [
    path('', contactView, name='home'),
    path('details/<int:pk>', ProjectDetailView.as_view(), name='details'),
    path('success', successView, name='success' ),
    path('proj/new/', ProjectCreateView.as_view(), name='proj_new'),
    path('<pk>/edit/',ProjectUpdateView.as_view(), name='proj_edit'),
    path('<pk>/delete/', ProjectDeleteView.as_view(), name='proj_delete'),
]