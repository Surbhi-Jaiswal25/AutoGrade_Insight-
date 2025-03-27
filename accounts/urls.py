from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
      path('homepage/', TemplateView.as_view(template_name = 'front/index.html'), name = 'home'),
      path ('loginpage/', views.CustomLoginView.as_view(), name = 'login'),
      path('registerpage/', views.register, name = 'register'),
      
]