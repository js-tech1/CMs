from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255,null = True)
    lastname=models.CharField(max_length=255,null = True)
    address=models.CharField(max_length=255,null = True)
    email = models.EmailField(null = True)
    password= models.CharField(max_length=255,null = True)
    
    def __str__(self):
        return self.name

    
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
class PostLike(models.Model):
    like = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    
    def __str__(self):
        return self.like