from django.urls import path
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path("reviews/", ReviewListCreateView.as_view(), name="list_create_review"),
    path(
        "reviews/<int:pk>/",
        ReviewRetrieveUpdateDestroyView.as_view(),
        name="retrieve_update_destroy_review",
    ),
]
