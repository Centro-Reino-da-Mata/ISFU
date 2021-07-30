# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
# from .models import Post, Category
# from .forms import PostForm, EditForm, ContactoForm
# from django.urls import reverse_lazy, reverse
# from django.http import HttpResponseRedirect
#
#
# def LikeView(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         liked = False
#     else:
#         post.likes.add(request.user)
#         liked = True
#
#     return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
#
#
#
# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
#     ordering = ['-post_date']
#
#     def get_context_data(self, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         context["cat_menu"] = cat_menu
#         return context
#
#
# def CategoryView(request, cats):
#     category_posts = Post.objects.filter(category=cats.replace('-', ' '))
#     return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '),
#                                                'category_posts': category_posts})
#
#
# class ArticleDetailView(DetailView):
#     model = Post
#     template_name = 'article_details.html'
#
#     def get_context_data(self, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
#
#         stuff = get_object_or_404(Post, id=self.kwargs['pk'])
#         total_likes = stuff.total_likes()
#
#         liked = False
#         if stuff.likes.filter(id=self.request.user.id).exists():
#             liked = True
#
#         context["cat_menu"] = cat_menu
#         context["total_likes"] = total_likes
#         context["liked"] = liked
#         return context
#
#
# class AddPostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'add_post.html'
#
# class AddCategoryView(CreateView):
#     model = Category
#     template_name = 'add_category.html'
#     fields = '__all__'
#
#
# class UpdatePostView(UpdateView):
#     model = Post
#     form_class = EditForm
#     template_name = 'update_post.html'
#
#
# class DeletePostView(DeleteView):
#     model = Post
#     template_name = 'delete_post.html'
#     success_url = reverse_lazy('home')
#
#
# class FormularioContacto(View):
#     def get(self,request):
#         form = ContactoForm()
#         contexto = {'form':form,}
#         return render(request,'contacto.html',contexto)
#
#     def post(self,request,*args,**kwargs):
#         form = ContactoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             contexto = {
#                 'form':form,
#             }
#             return render(request,'contacto.html',contexto)