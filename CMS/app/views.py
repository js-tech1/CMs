from django.shortcuts import render
from rest_framework import generics , permissions ,status
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.authentication import TokenAuthentication

class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostCreate(generics.CreateAPIView):
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     user = self.request.user

    #     # Check if the post owner and the user are the same
    #     if user != serializer.validated_data['owner']:
    #         return Response({'error': 'Post owner and user must be the same.'}, status=400)

    #     post = serializer.save(user)

    #         # Create a like for the post
    #     PostLike.objects.create(like='default', user=user, post=post)
    
        # Process the DELETE request for the post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        # Check if the post owner and the user are the same
        if user != serializer.validated_data['owner']:
            return Response({'error': 'Post owner and user must be the same.'}, status=400)

        post = serializer.save(owner=user)

        # Create a like for the post
        PostLike.objects.create(like='default', user=user, post=post)
    
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]  # Public posts can be accessed by any user

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)

# class LikeListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class LikeCreate(generics.CreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = LikeSerializer
    
class LikeCreateAPIView(generics.CreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = LikeSerializer

class LikeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = PostLike.objects.all()
    serializer_class = LikeSerializer

class LikeUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = LikeSerializer

class LikeDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = LikeSerializer