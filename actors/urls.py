from django.urls import path
from actors.views import ActorListCreateView, ActorRetrieveUpdateDestroyView

urlpatterns = [
    path("actors/", ActorListCreateView.as_view(), name="list_create_actor"),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyView.as_view(),
        name="retrieve_update_destroy_actor",
    ),
]
