from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .filters import ArticleFilter
from datetime import datetime
from .forms import ArticleForm
from django.urls import reverse_lazy


class ArticlesList(ListView):
    model = Article
    ordering = 'name'
    template_name = 'articles.html'
    context_object_name = 'articles'
    ordering = ['-datetime']
    paginate_by = 5


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class SearchList(ListView):
    model = Article
    ordering = 'name'
    template_name = 'search.html'
    context_object_name = 'search'
    ordering = ['-datetime']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticleFilter(self.request.GET, queryset)
        return self.filterset.qs


class ArticleCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ArticleForm
    model = Article
    template_name = 'create.html'


class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'create.html'


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = ('/articles/')