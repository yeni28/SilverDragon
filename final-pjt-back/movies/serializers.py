from rest_framework import serializers
from .models import *
# from accounts.serializers import UserSerializer


class HomeMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"
