from . import views
from django.urls import path
urlpatterns=[
    path('',views.index,name="index"),
    path('category/<int:n>/',views.category,name="category"),
    path('contact/',views.contact,name="contact"),
    path('search/',views.search,name="search"),
    path('<int:pk>/',views.view,name="view")
]
