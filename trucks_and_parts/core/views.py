from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import HomeProduct, Equipment, Truck, SparePart, Blog
from random import sample
from itertools import chain

# Create your views here.

def index(request):
    """
    View for the homepage.
    
    Retrieves and displays products, spare parts, trucks, equipment, and recent blogs. 
    Also, randomly samples some items to be displayed as featured products.
    
    Context:
        homepage_product: All products to be displayed on the homepage.
        featured_products: A list of randomly sampled featured products.
        servicing_parts: Spare parts of type 'Servicing Parts'.
        new_products: A list of new products including trucks, spare parts, and equipment.
        recent_blogs: A list of the most recent blog posts.
    """
    homepage_product = HomeProduct.objects.all()
    spare_parts = list(SparePart.objects.all())
    trucks = list(Truck.objects.all())

    # Querying for new products in different categories
    queryset1 = Truck.objects.filter(new=True)
    queryset2 = SparePart.objects.filter(new=True)
    queryset3 = Equipment.objects.filter(new=True)

    new_products = list(chain(queryset1, queryset2, queryset3))
    
    # Randomly sample featured products, ensuring the sample size doesn't exceed available items
    featured_products1 = sample(spare_parts, min(5, len(spare_parts)))
    featured_products2 = sample(trucks, min(3, len(trucks)))

    featured_products = featured_products1 + featured_products2
    servicing_parts = SparePart.objects.filter(type='Servicing Parts')

    # Querying for the 4 most recent blogs
    recent_blogs = Blog.objects.all().order_by('-date_posted')[:3]
    
    return render(request, 'core/home.html', {
        'homepage_product': homepage_product,
        'featured_products': featured_products,
        'servicing_parts': servicing_parts,
        'new_products': new_products,
        'recent_blogs': recent_blogs,
    })


def about(request):
    """
    View for the 'About Us' page.
    
    Renders the 'About Us' template to display static content.
    """
    return render(request, 'core/about_us.html')


def spare_parts(request, category=None, part_type=None):
    """
    View to list spare parts, optionally filtered by category and type.
    
    Retrieves all spare parts from the database and filters them based on the provided
    category and/or part type.
    
    Context:
        spare_parts: A list of spare parts filtered by category and/or type.
        selected_category: The category currently being filtered, if any.
        selected_type: The part type currently being filtered, if any.
    """
    # Querying for the 4 most recent blogs
    recent_blogs = Blog.objects.all().order_by('-date_posted')[:3]
    spare_parts = SparePart.objects.all()

    if part_type:
        spare_parts = spare_parts.filter(type__iexact=part_type)

    context = {
        'spare_parts': spare_parts,
        'selected_type': part_type,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'core/spare_parts.html', context)

def truck(request):
    """
    View to list all trucks.
    
    Retrieves all trucks from the database and renders them on the trucks page.
    
    Context:
        trucks: A list of all trucks.
    """
    trucks = Truck.objects.all()
    return render(request, 'core/truck.html', {'trucks': trucks})


def equipment(request):
    """
    View to list all equipment.
    
    Retrieves all equipment from the database and renders them on the equipment page.
    
    Context:
        equipments: A list of all equipment.
    """
    equipments = Equipment.objects.all()
    return render(request, 'core/equipment.html', {'equipments': equipments})


def truck_details(request, truck_id):
    """
    View to display details of a single truck.
    
    Retrieves a specific truck by its ID and also retrieves related products to suggest similar trucks.
    
    Args:
        truck_id: The ID of the truck to be displayed.
    
    Context:
        truck: The truck object that matches the provided ID.
        related_products: A list of related trucks to suggest to the user.
    """
    truck = get_object_or_404(Truck, id=truck_id)
    related_products = Truck.objects.exclude(id=truck_id)[:4]
    return render(request, 'core/truck_details.html', {'truck': truck, 'related_products': related_products})


def spare_part_details(request, spare_part_id):
    """
    View to display details of a single spare part.
    
    Retrieves a specific spare part by its ID and also retrieves related products to suggest similar spare parts.
    
    Args:
        spare_part_id: The ID of the spare part to be displayed.
    
    Context:
        spare_part: The spare part object that matches the provided ID.
        related_products: A list of related spare parts to suggest to the user.
    """
    spare_part = get_object_or_404(SparePart, id=spare_part_id)
    related_products = SparePart.objects.exclude(id=spare_part_id)[:4]
    return render(request, 'core/spare_part_details.html', {'spare_part': spare_part, 'related_products': related_products})


def equipment_details(request, equipment_id):
    """
    View to display details of a single piece of equipment.
    
    Retrieves a specific piece of equipment by its ID and also retrieves related equipment to suggest similar items.
    
    Args:
        equipment_id: The ID of the equipment to be displayed.
    
    Context:
        equipment: The equipment object that matches the provided ID.
        related_equipment: A list of related equipment to suggest to the user.
    """
    equipment = get_object_or_404(Equipment, id=equipment_id)
    related_equipment = Equipment.objects.exclude(id=equipment_id)[:4]
    return render(request, 'core/equipment_details.html', {'equipment': equipment, 'related_equipment': related_equipment})


def blog_list(request):
    """
    View to list all blog posts.
    
    Retrieves all blog posts, ordered by the most recent first, and renders them on the blog list page.
    
    Context:
        blogs: A list of all blogs, ordered by date posted in descending order.
    """
    blogs = Blog.objects.all().order_by('-date_posted')
    return render(request, 'core/blog_list.html', {'blogs': blogs})


def blog_details(request, blog_id):
    """
    View to display details of a single blog post.
    
    Retrieves a specific blog post by its ID and also retrieves recent blogs to suggest to the user.
    
    Args:
        blog_id: The ID of the blog post to be displayed.
    
    Context:
        blog: The blog object that matches the provided ID.
        recent_blogs: A list of the most recent blog posts excluding the current one.
    """
    blog = get_object_or_404(Blog, id=blog_id)
    recent_blogs = Blog.objects.exclude(id=blog_id).order_by('-date_posted')[:4]
    return render(request, 'core/blog_details.html', {'blog': blog, 'recent_blogs': recent_blogs})
