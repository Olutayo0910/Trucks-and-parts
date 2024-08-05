from django.contrib import admin
from django import forms
from .models import HomeProduct, Truck, SparePart, Equipment, Blog

# Custom form for Truck model to handle JSONField
class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = '__all__'
        widgets = {
            'details': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def clean_details(self):
        data = self.cleaned_data['details']
        # Optionally validate JSON data if needed
        return data
    
class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = '__all__'
        widgets = {
            'details': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def clean_details(self):
        data = self.cleaned_data['details']
        # Optionally validate JSON data if needed
        return data

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'details': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def clean_details(self):
        data = self.cleaned_data['details']
        # Optionally validate JSON data if needed
        return data
    
class HomeProductAdmin(admin.ModelAdmin):
    list_display = ('image',)  # Show image field in list view
    search_fields = ()  # No search fields
    list_filter = ()  # No filters

class TruckAdmin(admin.ModelAdmin):
    form = TruckForm
    list_display = ('name', 'category', 'type', 'description')  # Include description field if needed
    search_fields = ('name', 'category', 'type')
    list_filter = ('category', 'type')

class SparePartAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'type', 'description', 'price', 'old_price')
    search_fields = ('name', 'category', 'type')
    list_filter = ('category', 'type')

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'type', 'description')
    search_fields = ('name', 'category', 'type')
    list_filter = ('category', 'type')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'author')
    list_filter = ('date_posted',)

# Register your models with the custom admin classes
admin.site.register(HomeProduct, HomeProductAdmin)
admin.site.register(Truck, TruckAdmin)
admin.site.register(SparePart, SparePartAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Blog, BlogAdmin)
