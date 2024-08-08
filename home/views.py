from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Food, Category, CartItem

def home(request):
    return render(request, 'home.html')

def food_list(request):
    categories = Category.objects.all()
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods, 'categories': categories})

@login_required
def add_to_cart(request, food_id):
    food_item = get_object_or_404(Food, id=food_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        food=food_item,
        is_ordered=False
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'Added {food_item.name} to cart.')
    return redirect('food_list')

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user, is_ordered=False)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user, is_ordered=False)

    for item in cart_items:
        item.is_ordered = True
        item.save()

    return redirect('food_list')


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    foods = Food.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'foods': foods})

def about(request):
    return render(request, 'about.html')