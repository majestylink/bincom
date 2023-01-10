"""bincomTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from src import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('list_polls/', views.list_pools, name='list_polls'),
    path('summed_results/<int:lga_id>/', views.summed_results, name='summed_results'),
    # path('add_items/', views.add_items, name='add_items'),
    # path('update_items/<str:pk>/', views.update_items, name="update_items"),
    # path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('polling_unit_detail/<str:polling_unit_unique_id>/', views.polling_unit_detail, name="polling_unit_detail"),
    # path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
    # path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
    # path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
    # path('accounts/', include('registration.backends.default.urls')),
]
