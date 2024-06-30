from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('steps/', views.steps, name='steps'),
    path('adopt/', views.adopt, name='adopt'),
    path('adopt/details/<int:id>', views.details, name='details'),
    path('adopt/form/<int:pet_id>/', views.adopt_form, name='adopt_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('add_adopt/', views.add_adopt, name='add_adopt'),
    path('update_adopt/<int:pet_id>', views.update_adopt, name='update_adopt'),
    path('delete_adopt/<int:pet_id>', views.delete_adopt, name='delete_adopt'),
    path('adopt_request/', views.adopt_request, name="adopt_request"),
    path('volunteer_list/', views.volunteer_list, name="volunteer_list"),
]

