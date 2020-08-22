from django.urls import path
from .views import (
    AdsListView,
    AdsDetailView,
    AdsCreateView,
    AdsUpdateView,
    AdsDeleteView,
    UserAdsListView
)
from . import views

urlpatterns = [
    #ad
    path('', AdsListView.as_view() , name='Advertisements-home'),
    path('user/<str:username>', UserAdsListView.as_view() , name='user-ads'),
    path('ad/<pk>/', AdsDetailView.as_view(), name='Advertisements-detail'),
    path('new/', AdsCreateView.as_view(), name='Advertisements-create'),
    path('ad/<pk>/update/', AdsUpdateView.as_view(), name='Advertisements-update'),
    path('ad/<pk>/delete/', AdsDeleteView.as_view(), name='Advertisements-delete'),
    path('about/', views.about, name='Advertisements-about'),
	path('searchByCity/', views.searchByCity, name='Advertisements-by-city-api'),
]
