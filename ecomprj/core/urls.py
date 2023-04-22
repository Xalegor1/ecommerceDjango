from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'items_api', ProductViewSet)

urlpatterns = [

    # REST FRAMEWORK
    path('api/', include(router.urls)),


    # Homepage
    path('', views.index, name='index'),
    path('products/', views.product_list, name='products-list'),
    path('prod-detail/<pid>/', views.prod_detail_view, name='prod-detail'),

    # Category
    # path('category/', views.category_list_view, name="category-list"),
    path('category/<cid>/', views.prod_lst_categ_view, name="category-product-list"),

    # Tags
    path('products/tag/<slug:tag_slug>/', views.tag_list, name='tags'),


    # Search
    path('search/', views.search_view, name='search'),

    # Filter
    path("filter-products/", views.filter_product, name="filter-product"),

    # Add To Cart
    path("add-to-cart/", views.add_to_cart, name='add-to-cart'),

    # Cart Page URL
    path("cart/", views.cart_view, name='cart'),

    # Delete Item From Cart
    path("delete-from-cart/", views.delete_item_from_cart, name='delete-from-cart'),

    # Update Cart
    path("update-cart/", views.update_cart, name='update-cart'),

    # path('cart/update/', views.update_cart, name='update_cart'),

    

]



