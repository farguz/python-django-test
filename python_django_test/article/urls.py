from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index),
    path("", views.IndexView.as_view()),
    path(
        '<str:tags>/<int:article_id>/',
        views.TagPageView.as_view(),
        name='article'
        ),
    ]
