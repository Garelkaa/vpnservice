from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView


class MainView(TemplateView):
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Головна сторінка"
        return context
    