from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from movies.models import *


@api_view(['POST'])
def signup(request):
    print(request.data)
    password = request.data.get("password")
    password2 = request.data.get("password2")


    if password != password2:
        return Response({"error:비밀번호가 일치하지 않습니다"},status=status.HTTP_400_BAD_REQUEST)
    userinfo = {
        'username': request.data["username"],
        'password' : password
    }

    serializer = UserSerializer(data = request.data)

    if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # 사용자의 암호를 해쉬함수를 통해 바꿔줌(암호화)
            user.set_password(request.data.get("password"))
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    comment_list = person.replymoviecomment.all()
    like_movie_list = person.user_like_movie.all()
    s
    return Response()
