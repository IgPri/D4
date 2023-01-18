from django_filters import FilterSet, DateRangeFilter
from .models import Article


class ArticleFilter(FilterSet):
    datetime = DateRangeFilter
    class Meta:
        model = Article
        fields = {'name': ['icontains'],
                  'author': ['exact'],
                  'datetime': ['gt']}

