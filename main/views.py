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
import traceback

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
    product_list = Product.objects.all()

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
    try:
        print("=== DEBUG: get_products START ===")
        print(f"User: {request.user}")
        print(f"Authenticated: {request.user.is_authenticated}")
        print(f"Filter: {request.GET.get('filter', 'all')}")
        
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'User not authenticated'}, status=401)
        
        filter_type = request.GET.get("filter", "all")
        print(f"Filter type: {filter_type}")
        
        # Get products based on filter
        if filter_type == "my":
            product_list = Product.objects.filter(user=request.user)
        elif filter_type == "all":
            product_list = Product.objects.all()
        else:
            product_list = Product.objects.filter(category=filter_type)
        
        print(f"Products found: {product_list.count()}")
        
        # Convert to list first to avoid database queries in loop
        product_list = list(product_list)
        
        products_data = []
        for product in product_list:
            try:
                # Safe data extraction with defaults
                product_data = {
                    'id': product.id,
                    'name': getattr(product, 'name', 'No Name'),
                    'price': getattr(product, 'price', 0),
                    'description': getattr(product, 'description', 'No description'),
                    'thumbnail': getattr(product, 'thumbnail', ''),
                    'category': getattr(product, 'category', 'apparel'),
                    'category_display': product.get_category_display() if hasattr(product, 'get_category_display') else getattr(product, 'category', 'Unknown'),
                    'product_views': getattr(product, 'product_views', 0),
                    'is_featured': bool(getattr(product, 'is_featured', False)),
                    'is_product_hot': getattr(product, 'product_views', 0) > 25,
                    'created_at': product.created_at.strftime("%b %d, %Y") if hasattr(product, 'created_at') and product.created_at else "Unknown date",
                    'user': product.user.username if hasattr(product, 'user') and product.user else 'Anonymous',
                    'is_owner': hasattr(product, 'user') and product.user == request.user,
                }
                products_data.append(product_data)
            except Exception as e:
                print(f"Error processing product {getattr(product, 'id', 'unknown')}: {str(e)}")
                continue
        
        print("=== DEBUG: Successfully processed products ===")
        print(f"Returning {len(products_data)} products")
        
        return JsonResponse(products_data, safe=False)
        
    except Exception as e:
        print(f"=== DEBUG: CRITICAL ERROR in get_products ===")
        print(f"Error: {str(e)}")
        print("Full traceback:")
        print(traceback.format_exc())
        print("=== DEBUG: END ERROR ===")
        
        return JsonResponse({
            'error': 'Internal server error',
            'message': str(e)
        }, status=500)

@csrf_exempt
@login_required(login_url='/login/')
def add_product_entry_ajax(request):
    try:
        if request.method == 'POST':
            name = request.POST.get("name", "").strip()
            price = request.POST.get("price", "0")
            description = request.POST.get("description", "").strip()
            thumbnail = request.POST.get("thumbnail", "").strip()
            category = request.POST.get("category", "apparel")
            is_featured = request.POST.get("is_featured") == 'on'

            # Validation
            if not name:
                return JsonResponse({'status': 'error', 'message': 'Product name is required'})
            
            try:
                price = int(price)
            except (ValueError, TypeError):
                return JsonResponse({'status': 'error', 'message': 'Invalid price'})

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

        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
    except Exception as e:
        print(f"Error in add_product_entry_ajax: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f'Server error: {str(e)}'})

@csrf_exempt
@login_required(login_url='/login/')
def edit_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        
        if request.method == 'POST':
            product.name = request.POST.get("name", "").strip()
            price = request.POST.get("price", "0")
            product.description = request.POST.get("description", "").strip()
            product.thumbnail = request.POST.get("thumbnail", "").strip()
            product.category = request.POST.get("category", "apparel")
            product.is_featured = request.POST.get("is_featured") == 'on'

            # Validation
            if not product.name:
                return JsonResponse({'status': 'error', 'message': 'Product name is required'})
            
            try:
                product.price = int(price)
            except (ValueError, TypeError):
                return JsonResponse({'status': 'error', 'message': 'Invalid price'})

            product.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Product updated successfully!'
            })

        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
    except Exception as e:
        print(f"Error in edit_product_ajax: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f'Server error: {str(e)}'})

@csrf_exempt
@login_required(login_url='/login/')
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        
        if request.method == 'DELETE':
            product.delete()
            return JsonResponse({
                'status': 'success',
                'message': 'Product deleted successfully!'
            })

        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
    except Exception as e:
        print(f"Error in delete_product_ajax: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f'Server error: {str(e)}'})

@csrf_exempt
def register_ajax(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return JsonResponse({
                    'status': 'success',
                    'message': 'Your account has been successfully created!'
                })
            else:
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = [str(error) for error in error_list]
                return JsonResponse({
                    'status': 'error',
                    'errors': errors
                })
        
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
    except Exception as e:
        print(f"Error in register_ajax: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f'Server error: {str(e)}'})

@csrf_exempt
def login_ajax(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '').strip()
            
            if not username or not password:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Username and password are required'
                })
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
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
        
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
    except Exception as e:
        print(f"Error in login_ajax: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f'Server error: {str(e)}'})

@csrf_exempt
@login_required(login_url='/login/')
def logout_ajax(request):
    try:
        logout(request)
        response = JsonResponse({
            'status': 'success',
            'message': 'Logout successful!'
        })
        response.delete_cookie('last_login')
        return response
    
    except Exception as e:
        print(f"Error in logout_ajax: {str(e)}")
        return JsonResponse({'status': 'error', 'message': f'Server error: {str(e)}'})

@login_required(login_url='/login/')
def show_product(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        product.increment_views()

        context = {
            'product': product
        }
        return render(request, "product_detail.html", context)
    
    except Exception as e:
        print(f"Error in show_product: {str(e)}")
        return render(request, "404.html", status=404)

def show_xml(request):
    try:
        product_list = Product.objects.all()
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

def show_json(request):
    try:
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
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def urutin_harga(request):
    try:
        sort_order = request.GET.get('sort', 'asc')
        
        if sort_order == 'asc':
            products = Product.objects.all().order_by('price')
            message = 'Products sorted by price: Low to High'
        else:
            products = Product.objects.all().order_by('-price')
            message = 'Products sorted by price: High to Low'
        
        # Return JSON response instead of rendering template
        return JsonResponse({
            'status': 'success',
            'message': message,
            'sort_order': sort_order,
            'product_count': products.count()
        })
        
    except Exception as e:
        print(f"Error in urutin_harga: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Failed to sort products: {str(e)}'
        }, status=500)
