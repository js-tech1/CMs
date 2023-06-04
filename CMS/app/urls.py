
from django.urls import path
from .views import *


urlpatterns = [
    # path('', ListUser.as_view()),
    # path('createUser', userUser.as_view()),
    # path('<int:pk>', UpdateUser.as_view()),
    # path('deleteUser/<int:pk>', deleUser.as_view()),
    # # path('blog',addPost.as_view()),
    #  path('posts/', PostCreate.as_view(), name='post-create'),
    # path('posts/<int:pk>/', PostRetrieve.as_view(), name='post-retrieve'),
    # path('posts/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    # path('posts/<int:pk>/delete/', PostDestroy.as_view(), name='post-delete'),
    
    # path('blogs/', BlogCreate.as_view(), name='blog-create'),
    # path('blogs/<int:pk>/', BlogRetrieve.as_view(), name='blog-retrieve'),
    # path('blogs/<int:pk>/update/', BlogUpdate.as_view(), name='blog-update'),
    # path('blogs/<int:pk>/delete/', BlogDestroy.as_view(), name='blog-delete'),
    
    # path('like/<int:pk>', like.as_view()),
    # path('like/', LikeCreate.as_view()),
    # path('like/<int:pk>/', LikeRetrieve.as_view()),
    # path('like/<int:pk>/update/', LikeUpdate.as_view()),
    # path('like/<int:pk>/delete/', LikeDestroy.as_view()),
    
    
    
    path('', ListUser.as_view(), name='user-list'),
    path('createUser/', CreateUser.as_view(), name='user-create'),
    path('updateUser/<int:pk>/', UpdateUser.as_view(), name='user-update'),
    path('deleteUser/<int:pk>/', DeleteUser.as_view(), name='user-delete'),
    path('createPost/<int:pk>',PostCreate.as_view()),
    path('posts/', PostCreate.as_view(), name='post-create'),
    
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view(), name='post-retrieve'),
    path('posts/<int:pk>/update/', PostUpdateAPIView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),    
    path('like/', LikeCreate.as_view(), name='like-list'),
    path('like/create/', LikeCreateAPIView.as_view(), name='like-create'),
    path('like/<int:pk>/', LikeRetrieveAPIView.as_view(), name='like-retrieve'),
    path('like/<int:pk>/update/', LikeUpdateAPIView.as_view(), name='like-update'),
    path('like/<int:pk>/delete/', LikeDeleteAPIView.as_view(), name='like-delete'),
    
]