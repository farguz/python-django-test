from django.urls import path
from python_django_test.article.views import IndexView, ArticleView

urlpatterns = [
    # path('', views.index),
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article_view'),
    ]
