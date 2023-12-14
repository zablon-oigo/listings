from django.shortcuts import render,redirect
from .models import Listings
from .forms import ListingForm
from .filters import ListingFilter



def index(request):
    return render(request, 'listings/index.html')



def all_listings(request):
    listings=Listings.objects.all().order_by('-list_date')
    my_Filter = ListingFilter(request.GET, queryset=listings)
    listings = my_Filter.qs
    context={'listings':listings, 'my_Filter':my_Filter}
    return render(request, 'listings/all_listings.html',context)

def listing_detail(request, pk):
    listing=Listings.objects.get(id=pk)
    context={'listing':listing}
    return render(request, 'listings/listing_detail.html',context)

def update_listings(request,pk):
    listing=Listings.objects.get(id=pk)
    if request.method == "POST":
        form=ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', pk=listing.id)
    else:
        form=ListingForm(instance=listing)
    context={'form':form, 'listing':listing}
    return render(request, 'listings/update_listings.html',context)

def delete_listings(request,pk):
    listing=Listings.objects.get(id=pk)
    if request.method == "POST":
        listing.delete()
        return redirect('all_listings')
    context={'listing':listing}
    return render(request, 'listings/delete_listings.html',context)


def create_listings(request):
    if request.method == 'POST':
        form=ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing=form.save()
            return redirect('listing_detail', pk=listing.id)
    else:   
        form=ListingForm()
    context={'form':form}
    return render(request, 'listings/create_listings.html',context)


def my_listings(request):

    my_listings = Listings.objects.order_by('-list_date').filter(user=request.user)

    context = {'my_listings': my_listings}

    return render(request, 'listings/my_listings.html', context)