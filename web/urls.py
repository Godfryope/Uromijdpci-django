from django.urls import path
from .views import HomeView,BlogDetailView,BlogCreateView,BlogDeleteView,BlogUpdateView,SearchResultsView,successView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name='details'),
    path('proj/new/', BlogCreateView.as_view(), name='proj_new'),
    path('<slug>/edit/',BlogUpdateView.as_view(), name='proj_edit'),
    path('<slug>/delete/', BlogDeleteView.as_view(), name='proj_delete'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    # path("contact/", contactView, name="contact"),
    path("success/", successView.as_view(), name="success"),
]