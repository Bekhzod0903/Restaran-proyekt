from django.urls import path
from .views import home,food_list,add_to_cart,view_cart,place_order,category_detail,about,order_confirmation\
    ,increment_item, decrement_item, delete_cart,help_page


urlpatterns = [
    path('', home, name='home'),
    path('food/', food_list, name='food_list'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('place-order/', place_order, name='place_order'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('about/', about, name='about'),
    path('order-confirmation/', order_confirmation, name='order_confirmation'),
    path('cart/increment/<int:item_id>/', increment_item, name='increment_item'),
    path('cart/decrement/<int:item_id>/',decrement_item, name='decrement_item'),
    path('cart/delete/',delete_cart, name='delete_cart'),
    path('help/', help_page, name='help_page'),

]