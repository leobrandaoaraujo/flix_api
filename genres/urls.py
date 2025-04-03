from django.urls import path
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path("genres/", GenreListCreateView.as_view(), name="list_create_genre"),
    path(
        "genres/<int:pk>/",
        GenreRetrieveUpdateDestroyView.as_view(),
        name="retrieve_update_destroy_genre",
    ),
]
