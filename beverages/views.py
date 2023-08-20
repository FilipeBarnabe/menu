from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView

from .models import Beverage, BeverageType


# Create your views here.
class BeverageListView(ListView):
    model = Beverage


class BeverageTypeListView(ListView):
    queryset = BeverageType.objects.all()
