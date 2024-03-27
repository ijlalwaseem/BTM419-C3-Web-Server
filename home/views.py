from django.shortcuts import render, redirect
from .models import Dealership, Sale, Inventory, Inspection
from .forms import SaleForm, InventoryForm, InspectionForm

# Create your views here.
def index(request):
    """The home page for C3 Project."""
    return render(request, 'home/index.html')

def sales_dealerships(request):
    """show all dealerships"""
    dealershiplist=Dealership.objects.order_by('date_added')
    context={'sales_dealerships':dealershiplist}
    return render(request,'home/sales_dealerships.html',context)

def sales_dealership(request, dealership_id):
    """Show a single dealership and its entries."""
    mydealership = Dealership.objects.get(id=dealership_id)
    mysales = mydealership.sale_set.order_by('-date_added')
    context = {'sales_dealership': mydealership, 'sales': mysales}
    return render(request, 'home/sales_dealership.html', context)

def inventory_dealerships(request):
    """show all dealerships"""
    dealershiplist=Dealership.objects.order_by('date_added')
    context={'inventory_dealerships':dealershiplist}
    return render(request,'home/inventory_dealerships.html',context)

def inventory_dealership(request, dealership_id):
    """Show a single dealership and its entries."""
    mydealership = Dealership.objects.get(id=dealership_id)
    myinventorys = mydealership.inventory_set.order_by('-date_added')
    context = {'inventory_dealership': mydealership, 'inventorys': myinventorys}
    return render(request, 'home/inventory_dealership.html', context)

def inspections_dealerships(request):
    """show all dealerships"""
    dealershiplist=Dealership.objects.order_by('date_added')
    context={'inspections_dealerships':dealershiplist}
    return render(request,'home/inspections_dealerships.html',context)

def inspections_dealership(request, dealership_id):
    """Show a single dealership and its entries."""
    mydealership = Dealership.objects.get(id=dealership_id)
    myinspections = mydealership.inspection_set.order_by('-date_added')
    context = {'inspections_dealership': mydealership, 'inspections': myinspections}
    return render(request, 'home/inspections_dealership.html', context)

def new_sale(request, dealership_id):
    """Add a new sale entry."""
    dealership = Dealership.objects.get(id=dealership_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = SaleForm()
    else:
        # POST data submitted; process data.
        form = SaleForm(data=request.POST)
        if form.is_valid():
            new_sale = form.save(commit=False)
            new_sale.dealership = dealership
            new_sale.save()
            return redirect('home:sales_dealership', dealership_id=dealership_id)
               
    # Display a blank or invalid form.
    context = {'dealership': dealership, 'form': form}
    return render(request, 'home/new_sale.html', context)

def new_inventory(request, dealership_id):
    """Add a new inventory entry."""
    dealership = Dealership.objects.get(id=dealership_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = InventoryForm()
    else:
        # POST data submitted; process data.
        form = InventoryForm(data=request.POST)
        if form.is_valid():
            new_inventory = form.save(commit=False)
            new_inventory.dealership = dealership
            new_inventory.save()
            return redirect('home:inventory_dealership', dealership_id=dealership_id)
               
    # Display a blank or invalid form.
    context = {'dealership': dealership, 'form': form}
    return render(request, 'home/new_inventory.html', context)

def new_inspection(request, dealership_id):
    """Add a new inspection entry."""
    dealership = Dealership.objects.get(id=dealership_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = InspectionForm()
    else:
        # POST data submitted; process data.
        form = InspectionForm(data=request.POST)
        if form.is_valid():
            new_inspection = form.save(commit=False)
            new_inspection.dealership = dealership
            new_inspection.save()
            return redirect('home:inspections_dealership', dealership_id=dealership_id)
               
    # Display a blank or invalid form.
    context = {'dealership': dealership, 'form': form}
    return render(request, 'home/new_inspection.html', context)

def edit_sale(request, sale_id):
    """Edit an existing sale."""
    sale = Sale.objects.get(id=sale_id)
    dealership = sale.dealership    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = SaleForm(instance=sale)
    else:
        # POST data submitted; process data.
        form = SaleForm(instance=sale, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:sales_dealership', dealership_id=dealership.id)    
    context = {'sale': sale, 'dealership': dealership, 'form': form}
    return render(request, 'home/edit_sale.html', context)

def edit_inventory(request, inventory_id):
    """Edit an existing inventory."""
    inventory = Inventory.objects.get(id=inventory_id)
    dealership = inventory.dealership    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = InventoryForm(instance=inventory)
    else:
        # POST data submitted; process data.
        form = InventoryForm(instance=inventory, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:inventory_dealership', dealership_id=dealership.id)    
    context = {'inventory': inventory, 'dealership': dealership, 'form': form}
    return render(request, 'home/edit_inventory.html', context)

def edit_inspection(request, inspection_id):
    """Edit an existing inspection."""
    inspection = Inspection.objects.get(id=inspection_id)
    dealership = inspection.dealership    
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = InspectionForm(instance=inspection)
    else:
        # POST data submitted; process data.
        form = InspectionForm(instance=inspection, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:inspections_dealership', dealership_id=dealership.id)    
    context = {'inspection': inspection, 'dealership': dealership, 'form': form}
    return render(request, 'home/edit_inspection.html', context)