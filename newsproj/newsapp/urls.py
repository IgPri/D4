from django.urls import path
from .views import ArticlesList, ArticleDetail, SearchList, ArticleCreate, ArticleUpdate, ArticleDelete

urlpatterns = [
   path('', ArticlesList.as_view()),
   path('<int:pk>', ArticleDetail.as_view(), name='article'),
   path('create/', ArticleCreate.as_view(), name='create'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='delete'),
   path('search/', SearchList.as_view(), name='search'),
]


