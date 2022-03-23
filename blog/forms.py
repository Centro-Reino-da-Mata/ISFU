# from django import forms
# from .models import Post, Category
#
#
# choices = Category.objects.all().values_list('name', 'name')
#
# choice_list = []
#
# for item in choices:
#     choice_list.append(item)
#
#
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'author', 'category', 'body', 'snippet', 'header_image')
#
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de Post'}),
#             'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'alexander', 'type':'hidden'}),
#             'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#             'snippet': forms.Textarea(attrs={'class': 'form-control'}),
#         }
#
#
# class EditForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'body', 'snippet')
#
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de Post'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido del Post'}),
#             'snippet': forms.Textarea(attrs={'class': 'form-control'}),
#         }