"""
URL configuration for menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import (
    BeverageListView,
    BeverageDetailView,
    FullMenuListView,
    BeverageTypeListView,
)

app_name = "beverages"
urlpatterns = [
    path("full/", FullMenuListView.as_view(), name="full"),
    path("", BeverageTypeListView.as_view(), name="categories"),
    path("category/<int:pk>/", BeverageListView.as_view(), name="beverages"),
    path("beverage/<int:pk>", BeverageDetailView.as_view(), name="detail"),
]
