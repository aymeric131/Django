
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('about/',views.about),
    path('listings/',views.listings),
    path('contact/', views.contact),
]
