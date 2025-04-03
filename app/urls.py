from django.contrib import admin
from django.urls import path, include

# from genres.views import genre_list_create_view, genre_retrieve_update_destroy_view

"""
# Forma anterior, com Function Based Views.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("genres/", genre_list_create_view, name="list_create_genre"),
    path("genres/<int:pk>/", genre_retrieve_update_destroy_view, name="retrieve_genre"),
    path(
        "genres/<int:pk>/update/",
        genre_retrieve_update_destroy_view,
        name="update_genre",
    ),
    path(
        "genres/<int:pk>/delete/",
        genre_retrieve_update_destroy_view,
        name="destroy_genre",
    ),
]
"""

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("authentication.urls")),
    path("api/v1/", include("genres.urls")),
    path("api/v1/", include("actors.urls")),
    path("api/v1/", include("movies.urls")),
    path("api/v1/", include("reviews.urls")),
]
