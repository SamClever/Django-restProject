from django.urls import path,include
from .views import WatchListAV, WatchDetailsAV,StreamPlatformAV,StreamDetailsAV,ReviewDetail, ReviewList,StreamPlatformVS# Ensure views are imported correctly
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register ('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
   path('list', WatchListAV.as_view(), name='movie-list'),  # /movies/list
    path('list/<int:pk>/', WatchDetailsAV.as_view(), name='movie-details'),  # /movies/list/1/

    # path('stream', StreamPlatformAV.as_view(), name='stream'),  # /movies/stream
    # path('stream/<int:pk>/', StreamDetailsAV.as_view(), name='stream-details'),  # /movies/stream/1/
    
    # router
    path ('',include (router.urls)),
    
    path('review/', ReviewList.as_view(), name='review-list'),  # Optional: /movies/review/
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),  # /movies/review/1/

    # Add this path for reviews related to a stream
    path('stream/<int:pk>/review-create/', ReviewList.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='stream-review-list')
]
