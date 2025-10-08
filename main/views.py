from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm 
from main.models import Product
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

CATEGORY_CHOICES = [
    ('apparel', 'Apparel'),
    ('active_wear', 'Active Wear'),
    ('footwear', 'Footwear'),
    ('equipments', 'Equipments'),
    ('nutrition_supplement', 'Nutrition & Supplement'),
    ('accessories', 'Accessories'),
    ('exclusive', 'Exclusive Items'),
]

def register_page(request):
    """Halaman register (hanya menampilkan form)"""
    return render(request, 'register.html')

def login_page(request):
    """Halaman login (hanya menampilkan form)"""
    return render(request, 'login.html')

@login_required(login_url='/login/')
def home(request):
    context = {
        'npm': '2406413426',
        'name': 'Raihana Nur Azizah',
        'class': 'PBP D',
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'categories': CATEGORY_CHOICES,
    }
    return render(request, 'home.html', context)

@csrf_exempt
@login_required(login_url='/login/')
def get_products(request):
    filter_type = request.GET.get("filter", "all")
    
    if filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    elif filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(category=filter_type)
    
    products_data = []
    for product in product_list:
        products_data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'category_display': product.get_category_display(),
            'product_views': product.product_views,
            'is_featured': product.is_featured,
            'is_product_hot': product.is_product_hot,
            'created_at': product.created_at.strftime("%b %d, %Y"),
            'user': product.user.username if product.user else 'Anonymous',
            'is_owner': product.user == request.user,
        })
    
    return JsonResponse(products_data, safe=False)

@csrf_exempt
@login_required(login_url='/login/')
def add_product_entry_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")
        category = request.POST.get("category")
        is_featured = request.POST.get("is_featured") == 'on'

        new_product = Product(
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            is_featured=is_featured,
            user=request.user
        )
        new_product.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Product created successfully!',
            'id': new_product.id
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
@login_required(login_url='/login/')
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    
    if request.method == 'POST':
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.thumbnail = request.POST.get("thumbnail")
        product.category = request.POST.get("category")
        product.is_featured = request.POST.get("is_featured") == 'on'
        product.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Product updated successfully!'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
@login_required(login_url='/login/')
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    
    if request.method == 'DELETE':
        product.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Product deleted successfully!'
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Your account has been successfully created!'
            })
        else:
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({
                'status': 'error',
                'errors': errors
            })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response_data = {
                'status': 'success',
                'message': 'Login successful!'
            }
            response = JsonResponse(response_data)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid username or password.'
            })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
@login_required(login_url='/login/')
def logout_ajax(request):
    logout(request)
    response = JsonResponse({
        'status': 'success',
        'message': 'Logout successful!'
    })
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login/')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def register_page(request):
    """Halaman register (hanya menampilkan form)"""
    return render(request, 'register.html')

def login_page(request):
    """Halaman login (hanya menampilkan form)"""
    return render(request, 'login.html')