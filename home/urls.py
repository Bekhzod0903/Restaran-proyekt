from django.urls import path
from .views import home,food_list,add_to_cart,view_cart,place_order,category_detail,about

urlpatterns = [
    path('', home, name='home'),
    path('food/', food_list, name='food_list'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('place-order/', place_order, name='place_order'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('about/', about, name='about'),
]