from django.urls import path

from . import views


urlpatterns = [
   path('', views.index, name='index'),
    ##path('', views.login, name='login'),
   path('dictionary', views.DictionaryListView.as_view(), name='dictionary'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    #path('authors/', views.AuthorListView.as_view(), name='authors'),
    #path('author/<int:pk>',
    #     views.AuthorDetailView.as_view(), name='author-detail'),
]

