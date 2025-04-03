# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from genres.serializers import GenreSerializer
from genres.models import Genre
from app.permissions import GlobalDefaultPermissions

"""
@csrf_exempt
def genre_list_create_view(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        data = [{"id": genre.id, "name": genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        new_genre = Genre(name=data["name"])
        new_genre.save()
        return JsonResponse({"id": new_genre.id, "name": new_genre.name}, status=201)


@csrf_exempt
def genre_retrieve_update_destroy_view(request, pk):
    # genre = Genre.objects.get(pk=pk)
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == "GET":
        return JsonResponse({"id": genre.id, "name": genre.name}, status=201)
    elif request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        genre.name = data["name"]
        genre.save()
        return JsonResponse({"id": genre.id, "name": genre.name})
    elif request.method == "DELETE":
        genre_id = genre.id
        genre_name = genre.name
        genre.delete()
        return JsonResponse({"id": genre_id, "name": genre_name}, status=204)
"""


class GenreListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
