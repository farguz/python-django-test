from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={"article_id": 42, "tags": "python"}))
    
class TagPageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(
            request, "articles/index.html", context={"article_id": 42, "tags": "python"},
        )    
