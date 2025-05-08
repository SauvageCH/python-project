from django.urls import path
from . import views
#les routes principaux
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_contact, name='add_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]
