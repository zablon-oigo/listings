from django.urls import path 
from .views import (my_listings,index,all_listings,delete_listings,update_listings,create_listings,listing_detail)

app_name='listings'

urlpatterns=[
    path('',index,name='index'),
    path('all-listings/',all_listings,name='all_listings'),
    path('my-listings/',my_listings,name='my_listings'),
    path('create/',create_listings,name='new_listing'),
    path('update/<int:pk>/',update_listings,name='update_listings'),
    path('delete/<int:pk>/',delete_listings,name='delete_listings'),
    path('<int:pk>/',listing_detail,name='listing_detail'),
    
]