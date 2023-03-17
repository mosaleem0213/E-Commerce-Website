
from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index,name="shopHome"),
    path('about/', views.about,name="AboutUS"),
    path('contact/', views.contact,name="ContactUs"),
    path('search/', views.search,name="Search"),
    path('tracker/', views.treck,name="TrackingStatus"),
    path('products/<int:myid>', views.productView,name="ProductView"),
    path('checkout', views.checkout,name="Checkout"),
]
