from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseBadRequest
from .models import HomeProduct, Equipment, Truck, SparePart
from random import sample
from itertools import chain

# Create your views here.
def index(request):
    homepage_product = HomeProduct.objects.all()
    spare_parts = list(SparePart.objects.all())
    trucks = list(Truck.objects.all())
    
    queryset1 = Truck.objects.filter(new=True)
    queryset2 = SparePart.objects.filter(new=True)
    queryset3 = Equipment.objects.filter(new=True)

    new_products = list(chain(queryset1, queryset2, queryset3))
    
    # Sample randomly, handling the case where there are fewer items than requested
    featured_products1 = sample(spare_parts, min(5, len(spare_parts)))
    featured_products2 = sample(trucks, min(3, len(trucks)))

    featured_products = featured_products1 + featured_products2
    servicing_parts = SparePart.objects.filter(type='Servicing Parts')
    return render(request, 'core/home.html', {'homepage_product': homepage_product, 'featured_products': featured_products, 'servicing_parts': servicing_parts, 'new_products': new_products,})


def about(request):
    return render(request, 'core/about_us.html')

def spare_parts(request):
    spare_parts = SparePart.objects.all()
    return render(request, 'core/spare_parts.html', {'spare_parts':spare_parts})

def truck(request):
    trucks = Truck.objects.all()
    return render(request, 'core/truck.html', {'trucks':trucks})

def equipment(request):
    equipments = Equipment.objects.all()
    return render(request, 'core/truck.html', {'equipments':equipments})

def truck_details(request, truck_id):
    truck = get_object_or_404(Truck, id=truck_id)
    related_products = Truck.objects.exclude(id=truck_id)[:4]
    return render(request, 'core/truck_details.html', {'truck': truck,'related_products': related_products})

def spare_part_details(request, spare_part_id):
    spare_part = get_object_or_404(SparePart, id=spare_part_id)
    related_products = SparePart.objects.exclude(id=spare_part_id)[:4]
    return render(request, 'core/spare_part_details.html', {'spare_part': spare_part, 'related_products': related_products})

def equipment_details(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    related_equipment = Equipment.objects.exclude(id=equipment_id)[:4]
    return render(request, 'core/equipment_details.html', {'equipment': equipment, 'related_equipment': related_equipment})