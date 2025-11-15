from django.urls import path
from main.views import home, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register_ajax, login_ajax, logout_ajax, get_products, add_product_entry_ajax, edit_product_ajax, delete_product_ajax, register_page, login_page, urutin_harga, proxy_image, create_product_flutter, json_user_products

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('get-products/', get_products, name='get_products'),
    path('add-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product-ajax/<int:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('urutin-harga/', urutin_harga, name='urutin_harga'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),
    path('json-user-products/', json_user_products, name='json_user_products'),
    
    # AJAX endpoints
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('logout-ajax/', logout_ajax, name='logout_ajax'),
    
    # HTML pages (untuk menampilkan form)
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
]