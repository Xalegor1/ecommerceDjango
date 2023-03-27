from django.urls import path
from . import views


urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    path('products/', views.product_list, name='products-list'),
    path('prod-detail/<pid>/', views.prod_detail_view, name='prod-detail'),

    # Category
    path('category/', views.category_list_view, name="category-list"),
    path('category/<cid>/', views.prod_lst_categ_view, name="category-product-list"),

]


