from django.urls import path
from .views import BoxRecommendationView

urlpatterns = [
    path('orders/<int:order_id>/recommend-box/', BoxRecommendationView.as_view()),
]