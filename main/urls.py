from django.urls import path

from .views import *
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    # path('', MenuListView.as_view(), name='home'),
    # path('product/<str:slug>', views.menuDetail, name='product'),    
    # path('subcategories/<slug>', views.subCategory, name='subcategory'),
    # path('categories/<slug>', views.category, name='category'),
    # path('supcategories/<slug>', views.supcategory, name='supcategory'),
    path('interior/',views.interior,name='interior'),
    # path("search/", SearchResultsView.as_view(), name="search"),
]