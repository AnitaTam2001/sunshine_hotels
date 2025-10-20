from django.contrib import admin
from .models import Hotel, Booking

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'price_per_night', 'hotel_type', 'rating']
    list_filter = ['hotel_type', 'rating']
    search_fields = ['name', 'location']
    readonly_fields = ['created_at']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'hotel', 'check_in', 'check_out', 'total_price']
    list_filter = ['check_in', 'check_out']
    search_fields = ['customer_name', 'customer_email', 'hotel__name']
    readonly_fields = ['created_at']