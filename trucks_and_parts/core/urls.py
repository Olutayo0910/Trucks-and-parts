from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("spare_parts/", views.spare_parts, name="spare_parts"),
    path('spare_parts/type/<str:part_type>/', views.spare_parts, name='spare_parts_by_type'),
    path("truck/", views.truck, name="truck"),
    path("equipment/", views.equipment, name="equipment"),
    path('spare_part/<int:spare_part_id>/', views.spare_part_details, name='spare_part_details'),
    path('truck/<int:truck_id>/', views.truck_details, name='truck_details'),
    path('equipment/<int:equipment_id>/', views.equipment_details, name='equipment_details'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', views.blog_details, name='blog_details'),
]