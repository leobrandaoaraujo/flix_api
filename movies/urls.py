from django.urls import path
from movies.views import (
    MovieListCreateView,
    MovieRetrieveUpdateDestroyView,
    MovieStatsView,
)

urlpatterns = [
    path("movies/", MovieListCreateView.as_view(), name="list_create_movie"),
    path(
        "movies/<int:pk>/",
        MovieRetrieveUpdateDestroyView.as_view(),
        name="retrieve_update_destroy_movie",
    ),
    path("movies/stats/", MovieStatsView.as_view(), name="movie_stats"),
]
