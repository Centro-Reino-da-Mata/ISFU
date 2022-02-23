# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from ckeditor.fields import RichTextField
# from datetime import datetime, date


# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bio = models.TextField()
#     profile_pic = models.ImageField(null=True, blank=True, upload_to='profile/images/')
#     facebook_url = models.CharField(max_length=255, null=True, blank=True)
#     twitter_url = models.CharField(max_length=255, null=True, blank=True)
#     instagram_url = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return str(self.user)

#     def get_absolute_url(self):
#         return reverse('home')

# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     class Meta:
#         verbose_name = 'Categoria'
#         verbose_name_plural = 'Categorias'

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('home')


# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     header_image = models.ImageField(null=True, blank=True, upload_to='post/images/')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = RichTextField(blank=True, null=True)
#     post_date = models.DateField(auto_now_add=True, blank=True, null=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     snippet = models.CharField(max_length=255)
#     likes = models.ManyToManyField(User, related_name='blog_posts')

#     def total_likes(self):
#         return self.likes.count()

#     def __str__(self):
#         return self.title + ' | ' + str(self.author)

#     def get_absolute_url(self):
#         return reverse('home')