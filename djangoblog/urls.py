from django.urls import path, re_path
from . import views
from .views import HomeView, ArticleView, AddPost, privacyPolicy, cookiePolicy, PostsCategoryView, PostsCategoryListView


urlpatterns = [
    path('', views.HomeView, name='home'),
    # path('', HomeView.as_view(), name='home'),
    path('article/<slug>', ArticleView.as_view(), name='articleview'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    # re_path(r'^category$', views.category_list, name='category_list'),
    # re_path(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    path('privacy-policy/', privacyPolicy, name='privacypolicy'),
    path('cookie-policy/', cookiePolicy, name='cookiepolicy'),
    path('category/<postscategory>/', views.PostsCategoryView.as_view(), name='postscategory'),
    path('categorys/', views.PostsCategoryListView.as_view(), name='postscategorylist'),
    #re_path(r'^category/(?P<catslug>[\w\-]+)/$', PostsCategoryView, name='postscategory'),
   # path('category/<str:cats>', PostsCategoryView, name='postcategory'),
]
