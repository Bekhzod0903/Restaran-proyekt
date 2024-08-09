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
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        card_number = request.POST.get('card_number')
        cart_items = CartItem.objects.filter(user=request.user, is_ordered=False)

        for item in cart_items:
            item.is_ordered = True
            item.save()


        return redirect('order_confirmation')

    return render(request, 'place_order.html')


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    foods = Food.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'foods': foods})

def about(request):
    return render(request, 'about.html')


from django.shortcuts import render

def order_confirmation(request):
    return render(request, 'order_confirmation.html')


@login_required
def increment_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user, is_ordered=False)
    cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f'Increased quantity of {cart_item.food.name}.')
    return redirect('view_cart')

@login_required
def decrement_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user, is_ordered=False)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        messages.success(request, f'Decreased quantity of {cart_item.food.name}.')
    else:
        cart_item.delete()
        messages.success(request, f'Removed {cart_item.food.name} from cart.')
    return redirect('view_cart')

@login_required
def delete_cart(request):
    CartItem.objects.filter(user=request.user, is_ordered=False).delete()
    messages.success(request, 'All items have been removed from your cart.')
    return redirect('view_cart')


def help_page(request):
    return render(request, 'help.html')
