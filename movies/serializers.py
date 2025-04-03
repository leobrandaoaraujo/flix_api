from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                "O ano de lançamento do filme não pode ser mais antigo que 1900!"
            )
        return value

    def validate_resume(self, value):
        if len(value) > 255:
            raise serializers.ValidationError(
                "O resumo não pode conter mais que 512 caracteres!"
            )
        return value


class CustomMovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "genre",
            "actors",
            "release_date",
            "rate",
            "resume",
        ]

    def get_rate(self, obj):
        """
        reviews = obj.reviews.all()
        if reviews:
            sum_reviews = 0
            for review in reviews:
                sum_reviews += review.stars
            return round(sum_reviews / len(reviews), 1)
        return None
        """
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return round(rate, 1)
        return None
