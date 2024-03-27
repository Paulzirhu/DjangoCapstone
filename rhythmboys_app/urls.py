from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('discography/', views.discography, name='discography'),
    path('login/', auth_views.LoginView.as_view(template_name='rhythmboys_app/login.html'), name='login'),
    path('book-tickets/', views.book_tickets, name='book_tickets'),
    path('purchase-merchandise/', views.purchase_merchandise, name='purchase_merchandise'),
    path('choose-option/', views.choose_option, name='choose_option'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
