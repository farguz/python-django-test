from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from python_django_test.article.models import Article

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )
    
class TagPageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(
            request, "articles/index.html", context={"article_id": 42, "tags": "python"},
        )    

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )
