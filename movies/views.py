from django.db.models import Count, Avg
from rest_framework import response, status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from movies.serializers import MovieSerializer, CustomMovieSerializer
from movies.models import Movie
from reviews.models import Review
from app.permissions import GlobalDefaultPermissions


class MovieListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CustomMovieSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CustomMovieSerializer
        return MovieSerializer


class MovieStatsView(APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        total_by_genre = self.queryset.values("genre__name").annotate(count=Count("id"))
        total_reviews = Review.objects.count()
        average_stars = round(
            Review.objects.aggregate(avg_stars=Avg("stars"))["avg_stars"], 1
        )
        return response.Response(
            data={
                "total_movies": total_movies,
                "total_by_genre": total_by_genre,
                "total_reviews": total_reviews,
                "average_stars": average_stars if average_stars else 0,
            },
            status=status.HTTP_200_OK,
        )
