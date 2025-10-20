from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Hotel, Booking
from datetime import datetime, timedelta
import json

def home(request):
    featured_hotels = Hotel.objects.all()[:6]
    context = {
        'featured_hotels': featured_hotels,
    }
    return render(request, 'home.html', context)

def hotel_list(request):
    hotels = Hotel.objects.all()
    hotel_types = Hotel.HOTEL_TYPES
    
    # Filtering
    hotel_type = request.GET.get('type')
    if hotel_type:
        hotels = hotels.filter(hotel_type=hotel_type)
    
    # Sorting
    sort = request.GET.get('sort', 'name')
    if sort == 'price_low':
        hotels = hotels.order_by('price_per_night')
    elif sort == 'price_high':
        hotels = hotels.order_by('-price_per_night')
    elif sort == 'rating':
        hotels = hotels.order_by('-rating')
    else:
        hotels = hotels.order_by('name')
    
    context = {
        'hotels': hotels,
        'hotel_types': hotel_types,
        'selected_type': hotel_type,
        'sort': sort,
    }
    return render(request, 'hotels/hotel_list.html', context)

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    similar_hotels = Hotel.objects.filter(hotel_type=hotel.hotel_type).exclude(id=hotel_id)[:4]
    
    context = {
        'hotel': hotel,
        'similar_hotels': similar_hotels,
    }
    return render(request, 'hotels/hotel_detail.html', context)

def search_hotels(request):
    query = request.GET.get('q', '')
    location = request.GET.get('location', '')
    
    hotels = Hotel.objects.all()
    
    if query:
        hotels = hotels.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(amenities__icontains=query)
        )
    
    if location:
        hotels = hotels.filter(location__icontains=location)
    
    context = {
        'hotels': hotels,
        'query': query,
        'location': location,
    }
    return render(request, 'hotels/search_results.html', context)

def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = int(request.POST.get('guests', 1))
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        
        # Calculate total price
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
        nights = (check_out_date - check_in_date).days
        total_price = hotel.price_per_night * nights
        
        # Create booking
        booking = Booking.objects.create(
            hotel=hotel,
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            customer_name=customer_name,
            customer_email=customer_email,
            total_price=total_price
        )
        
        return redirect('booking_success', booking_id=booking.id)
    
    # Default dates (check-in: tomorrow, check-out: day after tomorrow)
    default_check_in = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    default_check_out = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
    
    context = {
        'hotel': hotel,
        'default_check_in': default_check_in,
        'default_check_out': default_check_out,
    }
    return render(request, 'hotels/booking.html', context)

def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        'booking': booking,
    }
    return render(request, 'hotels/booking_success.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')