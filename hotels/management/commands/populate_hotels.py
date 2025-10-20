from django.core.management.base import BaseCommand
from hotels.models import Hotel

class Command(BaseCommand):
    help = 'Populate database with sample hotels'

    def handle(self, *args, **options):
        hotels_data = [
            {
                'name': 'Sunshine Beach Resort',
                'location': 'Miami, Florida',
                'description': 'Luxury beachfront resort with stunning ocean views and world-class amenities. Perfect for romantic getaways and family vacations.',
                'price_per_night': 299.99,
                'image_url': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                'hotel_type': 'beach',
                'rating': 4.8,
                'amenities': 'Free WiFi, Swimming Pool, Spa, Restaurant, Bar, Gym, Beach Access, Kids Club'
            },
            {
                'name': 'City Lights Hotel',
                'location': 'New York, New York',
                'description': 'Modern hotel in the heart of Manhattan with breathtaking city views. Ideal for business travelers and urban explorers.',
                'price_per_night': 349.99,
                'image_url': 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                'hotel_type': 'city',
                'rating': 4.5,
                'amenities': 'Free WiFi, Restaurant, Gym, Business Center, Concierge, Room Service'
            },
            {
                'name': 'Mountain View Boutique',
                'location': 'Aspen, Colorado',
                'description': 'Charming boutique hotel nestled in the mountains with cozy accommodations and ski-in/ski-out access.',
                'price_per_night': 279.99,
                'image_url': 'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                'hotel_type': 'boutique',
                'rating': 4.7,
                'amenities': 'Free WiFi, Fireplace, Hot Tub, Restaurant, Ski Storage, Mountain Views'
            },
            {
                'name': 'Royal Palm Luxury Resort',
                'location': 'Maui, Hawaii',
                'description': 'Five-star luxury resort featuring private villas, exceptional service, and pristine beaches.',
                'price_per_night': 599.99,
                'image_url': 'https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                'hotel_type': 'luxury',
                'rating': 4.9,
                'amenities': 'Free WiFi, Private Pool, Spa, Multiple Restaurants, Golf Course, Beach Club, Butler Service'
            },
            {
                'name': 'Desert Oasis Resort',
                'location': 'Scottsdale, Arizona',
                'description': 'Luxurious desert retreat with stunning mountain views, premium spa services, and championship golf.',
                'price_per_night': 329.99,
                'image_url': 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                'hotel_type': 'luxury',
                'rating': 4.6,
                'amenities': 'Free WiFi, Spa, Golf Course, Pool, Fine Dining, Tennis Courts, Desert Tours'
            },
            {
                'name': 'Historic Grand Hotel',
                'location': 'Charleston, South Carolina',
                'description': 'Elegant historic hotel with classic architecture, modern comforts, and Southern hospitality.',
                'price_per_night': 229.99,
                'image_url': 'https://images.unsplash.com/photo-1584132967334-10e028bd69f7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80',
                'hotel_type': 'boutique',
                'rating': 4.4,
                'amenities': 'Free WiFi, Historic Charm, Restaurant, Garden, Library, Afternoon Tea'
            },
        ]

        # Clear existing hotels
        Hotel.objects.all().delete()

        for hotel_data in hotels_data:
            Hotel.objects.create(**hotel_data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated {len(hotels_data)} hotels with sample data')
        )