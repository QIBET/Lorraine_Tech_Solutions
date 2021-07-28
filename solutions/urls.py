from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('register/', views.register, name="register"),
	path('login/', views.loginUser, name="login"), 
    path('logout/',views.logoutUser,name="logout") ,
    path('spares/', views.get_spares,name='spares'),
    path('new_phone/', views.new_phone, name='newphone'),
    path('new_laptops/', views.new_laptop, name='new_laptops'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact_us,name='contact')


]