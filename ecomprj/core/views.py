from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category, Vendor, ProductImages, CartOrder, CartOrderItems, ProductReview, WishList, Address
from taggit.models import Tag
from django.template.loader import render_to_string
from django.http import JsonResponse


def index(request):
    products = Product.objects.all().order_by("-id")
    categories = Category.objects.all()

    context = {
        "products": products,
        "categories": categories

    }
    return render(request, 'index.html', context)


def product_list(request):
    products = Product.objects.filter(product_status="published")
    context = {
        "products": products
    }
    return render(request, 'products-list.html', context)



def category_list_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "category-list.html", context)


def prod_lst_categ_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)
    mama = Category.objects.all()
    count = Category.objects.filter(cid=cid).count()

    context = {
        "category": category,
        "products": products,
        "categories": mama,
        'count': count
    }
    return render(request, "category-prd-lst.html", context)


def prod_detail_view(request, pid):
    # product = Product.objects.get(pid=pid)
    product = get_object_or_404(Product, pid=pid)
    p_image = product.p_images.all()

    products = Product.objects.filter(category=product.category).exclude(pid=pid)

    # Getting all reviews
    reviews = ProductReview.objects.filter(product=product, )

    context = {
        "prod": product,
        "p_image": p_image,
        'reviews': reviews,
        "products": products,
    }
    return render(request, "product-detail.html", context)


def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="published").order_by('-id')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])

    context = {
        "products": products, 
        "tag": tag, 
        
    }
    return render(request, "tag.html", context)




def search_view(request):
    query = request.GET.get("q")
    products = Product.objects.filter(title__icontains=query).order_by("-date")

    context = {
        "products": products, 
        "query": query,
    }

    return render(request, "search.html", context)


def filter_product(request):
    categories = request.GET.getlist('category[]')
    
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']

    products = Product.objects.filter(product_status="published").order_by("-id").distinct()

    products = products.filter(price__gte=min_price)
    products = products.filter(price__lte=max_price)


    if len(categories) > 0:
        products = products.filter(category__id__in=categories).distinct()  

    data = render_to_string("async/zov.html", {"products": products})
    return JsonResponse({"data": data})



def add_to_cart(request):
    cart_product = {}

    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'pid': request.GET['pid'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data 
    else:
        request.session['cart_data_obj'] = cart_product               
    return JsonResponse({'data': request.session['cart_data_obj'], 'totalcartitems': len(request.session['cart_data_obj'])})



def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, 'cart.html', {'cart_data': request.session['cart_data_obj'], 
                                             'totalcartitems': len(request.session['cart_data_obj']), 
                                             'cart_total_amount': cart_total_amount
                                             })
    else:
        return render(request, 'cart-empty.html')
    

def delete_item_from_cart(request):
    product_id = str(request.GET['id'])
    if 'cart_data_obj' in request.session:
        if product_id in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            del request.session['cart_data_obj'][product_id]
            request.session['cart_data_obj'] = cart_data

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for p_id, item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])

    context = render_to_string("async/cart-list.html", {'cart_data': request.session['cart_data_obj'], 
                                                  'totalcartitems': len(request.session['cart_data_obj']), 
                                                  'cart_total_amount': cart_total_amount
                                                  })            
    return JsonResponse({"data": context, 'totalcartitems': len(request.session['cart_data_obj'])})
