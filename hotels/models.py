from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Hotel(models.Model):
    HOTEL_TYPES = [
        ('beach', 'Beach Resort'),
        ('city', 'City Hotel'),
        ('boutique', 'Boutique Hotel'),
        ('luxury', 'Luxury Resort'),
    ]
    
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    hotel_type = models.CharField(max_length=20, choices=HOTEL_TYPES)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    amenities = models.TextField(help_text="Comma separated list of amenities")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_image_url(self):
        """Return image URL, preferring local image over URL"""
        if self.image and self.image.url:
            return self.image.url
        elif self.image_url:
            return self.image_url
        else:
            return "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
    
    def get_amenities_list(self):
        return [amenity.strip() for amenity in self.amenities.split(',')]
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.hotel.name}"