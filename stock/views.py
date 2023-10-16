from django.shortcuts import render, redirect
from .models import StockItem, SoldItem, AvailableStock
from django.http import HttpResponse
from django.template import loader
from .forms import StockForm, SaleForm

def register_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)  # Use your stock form or a regular form
        if form.is_valid():
            # Get the quantity from the form data
            quantity = form.cleaned_data['quantity']

            # Create and save the stock item
            stock_item = AvailableStock(quantity=quantity)
            stock_item.save()

            # Optionally, you can provide additional information and redirect
            return redirect('view_stock')  # Replace 'success_page' with your desired success page URL

    else:
        form = StockForm()  # Use your stock form or a regular form

    return render(request, 'stock/register_stock.html', {'form': form})


def view_stock(request):
    stock_items = StockItem.objects.all()
    return render(request, 'stock/view_stock.html', {'stock_items': stock_items})




def register_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)  # Use your sale form or a regular form
        if form.is_valid():
            # Get the quantity sold from the form data
            quantity_sold = form.cleaned_data['quantity_sold']

            # Ensure that you have enough stock available
            available_stock = AvailableStock.objects.first()  # Adjust your query as needed

            if available_stock and available_stock.quantity >= quantity_sold:
                # Deduct the sold quantity from available stock
                available_stock.quantity -= quantity_sold
                available_stock.save()

                # Create a sold item record
                sold_item = SoldItem(quantity_sold=quantity_sold)
                sold_item.save()

                # Optionally, you can provide additional information and redirect
                return redirect('view_sold_items')  # Replace 'success_page' with your desired success page URL
            else:
                # Handle the case when there's not enough stock available
                return render(request, 'stock/insufficient_stock.html')

    else:
        form = SaleForm()  # Use your sale form or a regular form

    return render(request, 'stock/register_sale.html', {'form': form})

"""
def register_sold_item(request):
    if request.method == 'POST':
        stock_item_id = request.POST['stock_item']
        quantity = int(request.POST['quantity'])
        stock_item = StockItem.objects.get(pk=stock_item_id)
        available_stock = AvailableStock.objects.get(stock_item=stock_item)
        if available_stock.quantity >= quantity:
            available_stock.quantity -= quantity
            available_stock.save()
            sold_item = SoldItem(stock_item=stock_item, quantity=quantity)
            sold_item.save()
            return redirect('view_sold_items')
        else:
            return HttpResponse('Not enough stock available.')
    stock_items = StockItem.objects.all()
    return render(request, 'stock/register_sold_item.html', {'stock_items': stock_items})
"""
    
def view_sold_items(request):
    sold_items = SoldItem.objects.all()
    return render(request, 'stock/view_sold_items.html', {'sold_items': sold_items})

def view_available_stock(request):
    available_stock = AvailableStock.objects.all()
    return render(request, 'stock/view_available_stock.html', {'available_stock': available_stock})
