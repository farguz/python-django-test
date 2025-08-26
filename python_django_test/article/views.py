from django.shortcuts import render
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
