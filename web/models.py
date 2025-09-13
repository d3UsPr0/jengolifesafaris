from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = CKEditor5Field(config_name='default')
    image = models.ImageField(upload_to='destinations/')
    best_time_to_visit = models.CharField(max_length=200)
    wildlife = models.TextField(help_text="Common wildlife sightings")
    is_popular = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class SafariPackage(models.Model):
    PACKAGE_TYPES = (
        ('family', 'Family Safari'),
        ('luxury', 'Luxury Safari'),
        ('adventure', 'Adventure Safari'),
        ('honeymoon', 'Honeymoon Safari'),
        ('group', 'Group Safari'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.TextField()
    detailed_description = CKEditor5Field(config_name='default')
    duration_days = models.IntegerField()
    duration_nights = models.IntegerField()
    max_people = models.IntegerField()
    destinations = models.ManyToManyField(Destination, related_name="safari_packages")
    price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    package_type = models.CharField(max_length=20, choices=PACKAGE_TYPES)
    featured_image = models.ImageField(upload_to='safari_packages/')
    is_featured = models.BooleanField(default=False)
    included = models.TextField(help_text="List of included services (comma separated)")
    not_included = models.TextField(help_text="List of excluded services (comma separated)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class ItineraryDay(models.Model):
    safari_package = models.ForeignKey(SafariPackage, on_delete=models.CASCADE, related_name='itinerary_days')
    day_number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    accommodation = models.CharField(max_length=200, blank=True)
    meals_included = models.CharField(max_length=100, blank=True)
    activities = models.TextField(blank=True)
    
    class Meta:
        ordering = ['day_number']
    
    def __str__(self):
        return f"Day {self.day_number}: {self.title}"

class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('wildlife', 'Wildlife'),
        ('tips', 'Travel Tips'),
        ('culture', 'Local Culture'),
        ('conservation', 'Conservation'),
        ('birding', 'Bird Watching'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField()
    content = CKEditor5Field(config_name='default')
    featured_image = models.ImageField(upload_to='blog/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read_time = models.IntegerField(help_text="Reading time in minutes")
    published_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    tags = models.CharField(max_length=200, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Inquiry(models.Model):
    INQUIRY_STATUS = (
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('quoted', 'Quoted'),
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
    )
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    safari_package = models.ForeignKey(SafariPackage, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_adults = models.IntegerField(default=1)
    number_of_children = models.IntegerField(default=0)
    preferred_travel_date = models.DateField(null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=INQUIRY_STATUS, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    
    def __str__(self):
        return f"Inquiry from {self.name} - {self.created_at}"

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    category = models.CharField(max_length=50, default='general')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'question']
    
    def __str__(self):
        return self.question

class GalleryImage(models.Model):
    IMAGE_CATEGORIES = (
        ('wildlife', 'Wildlife'),
        ('landscape', 'Landscape'),
        ('accommodation', 'Accommodation'),
        ('cultural', 'Cultural'),
        ('activities', 'Activities'),
    )
    
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=IMAGE_CATEGORIES)
    caption = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="Jengo Life Safaris")
    contact_email = models.EmailField(default="info@jengolifesafaris.com")
    contact_phone = models.CharField(max_length=20, default="+255 788 822 792")
    address = models.TextField(default="123 Safari Road, Arusha, Tanzania")
    office_hours = models.TextField(default="Monday - Friday: 8:00 AM - 6:00 PM\nSaturday: 9:00 AM - 4:00 PM\nSunday: Closed")
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    about_us = CKEditor5Field(config_name='default', blank=True)
    terms_conditions = CKEditor5Field(config_name='default', blank=True)
    privacy_policy = CKEditor5Field(config_name='default', blank=True)

    
    def __str__(self):
        return "Site Settings"
    
    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
        
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/')
    experience = models.IntegerField(help_text="Years of experience")
    expertise = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name