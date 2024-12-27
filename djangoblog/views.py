from typing import Any
from unicodedata import category
from urllib import request
from urllib.request import Request
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, PostsCategory
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .serializers import PostsSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#def home(request):
 #   return render(request, 'home.html', {})

 # class based
# def category_list(request):
#     categories = Category.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)

#     return render (request, 'category_list.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

# def category_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)

#     return render(request, 'category_detail.html', {'category': category}) # in this template, you will have access to category and posts under that category by (category.post_set).

# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
#     ordering = ['-create_date', '-pk']


def HomeView(request):
    posts = Post.objects.all()  # fetching all post objects from database
    p = Paginator(posts, 6)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
        
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    # sending the page object to index.html
    return render(request, 'home.html', context)

class ArticleView(LoginRequiredMixin, DetailView):
    login_url = '/account/login'
    model = Post
    template_name = 'details.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    #fields = ('title', 'body')
    
def privacyPolicy(request):
    return render(request, 'privacy-policy.html')

def cookiePolicy(request):
    return render(request, 'cookie-policy.html')

# def PostsCategoryView(request, cats):
#     postscategory_posts = Post.objects.filter(postscategory = cats).values('catname')
#     return render(request, 'category_detail.html', {'cats':cats, 'postscategory_posts':postscategory_posts})

class PostsCategoryView(ListView):
    template_name = 'category_detail.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat':self.kwargs['postscategory'],
            'posts': Post.objects.filter(postscategory__catname = self.kwargs['postscategory'])
        }
        return content
    
class PostsCategoryListView(ListView):
    model = PostsCategory
    template_name = 'category_lists.html'
    context_object_name = 'catslist'

    # def get_queryset(self):
    #     content = {
    #         'cat':self.kwargs['postscategory'],
    #         'posts': Post.objects.filter(postscategory__catname = self.kwargs['postscategory'])
    #     }
    #     return content