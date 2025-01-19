from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Supplier, SaleOrder, StockMovement
from django.db.models import Sum
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

# Add Product
def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category = request.POST['category']
        price = request.POST['price']
        stock_quantity = request.POST['stock_quantity']
        supplier_id = request.POST['supplier']
        
        if Product.objects.filter(name=name).exists():
            messages.error(request, "Product with this name already exists.")
        else:
            supplier = get_object_or_404(Supplier, id=supplier_id)
            Product.objects.create(
                name=name, description=description, category=category,
                price=price, stock_quantity=stock_quantity, supplier=supplier
            )
            messages.success(request, "Product added successfully!")
            return redirect('list_products')
    
    suppliers = Supplier.objects.all()
    return render(request, 'add_product.html', {'suppliers': suppliers})


# List Products
def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})


# Add Supplier
def add_supplier(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        
        if Supplier.objects.filter(email=email).exists() or Supplier.objects.filter(phone=phone).exists():
            messages.error(request, "Supplier with this email or phone already exists.")
        else:
            Supplier.objects.create(name=name, email=email, phone=phone, address=address)
            messages.success(request, "Supplier added successfully!")
            return redirect('list_suppliers')
    
    return render(request, 'add_supplier.html')


# List Suppliers
def list_suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'list_suppliers.html', {'suppliers': suppliers})


# Add Stock Movement
def add_stock_movement(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        quantity = int(request.POST['quantity'])
        movement_type = request.POST['movement_type']
        notes = request.POST['notes']
        
        product = get_object_or_404(Product, id=product_id)
        if movement_type == 'Out' and product.stock_quantity < quantity:
            messages.error(request, "Insufficient stock.")
        else:
            StockMovement.objects.create(
                product=product, quantity=quantity, movement_type=movement_type, notes=notes
            )
            if movement_type == 'In':
                product.stock_quantity += quantity
            elif movement_type == 'Out':
                product.stock_quantity -= quantity
            product.save()
            messages.success(request, "Stock movement recorded successfully!")
            return redirect('list_products')
    
    products = Product.objects.all()
    return render(request, 'add_stock_movement.html', {'products': products})


# Create Sale Order
def create_sale_order(request):
    if request.method == 'POST':
        product_id = request.POST['product']
        quantity = int(request.POST['quantity'])
        product = get_object_or_404(Product, id=product_id)
        
        if product.stock_quantity < quantity:
            messages.error(request, "Insufficient stock.")
        else:
            total_price = quantity * float(product.price)
            SaleOrder.objects.create(
                product=product, quantity=quantity, total_price=total_price, status='Pending'
            )
            product.stock_quantity -= quantity
            product.save()
            messages.success(request, "Sale order created successfully!")
            return redirect('list_sale_orders')
    
    products = Product.objects.all()
    return render(request, 'create_sale_order.html', {'products': products})


# Cancel Sale Order
def cancel_sale_order(request, order_id):
    order = get_object_or_404(SaleOrder, id=order_id)
    order.status = 'Cancelled'
    order.product.stock_quantity += order.quantity
    order.product.save()
    order.save()
    messages.success(request, "Sale order cancelled successfully!")
    return redirect('list_sale_orders')


# Complete Sale Order
def complete_sale_order(request, order_id):
    order = get_object_or_404(SaleOrder, id=order_id)
    order.status = 'Completed'
    order.save()
    messages.success(request, "Sale order completed successfully!")
    return redirect('list_sale_orders')


# List Sale Orders
def list_sale_orders(request):
    sale_orders = SaleOrder.objects.all()
    return render(request, 'list_sale_orders.html', {'sale_orders': sale_orders})


# Stock Level Check
def stock_level_check(request):
    products = Product.objects.all()
    return render(request, 'stock_level_check.html', {'products': products})
