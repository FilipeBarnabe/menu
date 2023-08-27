from typing import Any, Dict
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Beverage, BeverageType


# Create your views here.
class BeverageListView(ListView):
    model = Beverage

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(beverage_type__id=self.kwargs["pk"])

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["category"] = list(
            BeverageType.objects.filter(id=self.kwargs["pk"]).values_list(
                "type_name", flat=True
            )
        )[0]
        return context


class BeverageDetailView(DetailView):
    model = Beverage


class BeverageTypeListView(ListView):
    model = BeverageType


class BeverageTypeDetailView(DetailView):
    queryset = BeverageType.objects.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class FullMenuListView(ListView):
    queryset = BeverageType.objects.all()
    template_name = "beverages/full_menu_list.html"
