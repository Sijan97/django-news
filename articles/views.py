from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(ListView):
    """ List view definition for articles. """
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    """ View definition for article detail view. """
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView):
    """ View definition to edit article. """
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body', 'cover')

class ArticleDeleteView(DeleteView):
    """ View definition to delete an article. """
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

# class ArticleCreateView(CreateView):
#     """ Defining custom create view for article. """
#     model = Article
#     template_name = 'article_new.html'
#     fields = ('title', 'body', 'cover')