from django.contrib import admin
from .models import (
    Destination, SafariPackage, ItineraryDay, BlogPost,
    Inquiry, FAQ, GalleryImage, SiteSetting,
    Subscriber, TeamMember, Testimonial
)


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_popular", "best_time_to_visit")
    list_filter = ("is_popular",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


class ItineraryDayInline(admin.TabularInline):  # Inline editing inside SafariPackage
    model = ItineraryDay
    extra = 1


@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    list_display = ("title", "package_type", "price_per_person", "is_featured", "created_at")
    list_filter = ("package_type", "is_featured", "destinations")
    search_fields = ("title", "short_description", "detailed_description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ItineraryDayInline]


@admin.register(ItineraryDay)
class ItineraryDayAdmin(admin.ModelAdmin):
    list_display = ("safari_package", "day_number", "title")
    list_filter = ("safari_package",)
    search_fields = ("title", "description")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "is_published", "published_date")
    list_filter = ("category", "is_published")
    search_fields = ("title", "excerpt", "tags")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "safari_package", "status", "created_at")
    list_filter = ("status", "safari_package")
    search_fields = ("name", "email", "message")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "category", "is_active", "order")
    list_filter = ("is_active", "category")
    search_fields = ("question", "answer")
    ordering = ("order",)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "location", "is_featured", "uploaded_at")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "caption", "location")


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("site_name", "contact_email", "contact_phone")
    search_fields = ("site_name", "contact_email", "contact_phone")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("client_name", "country", "rating", "safari_package", "is_featured", "created_at")
    list_filter = ("rating", "is_featured", "safari_package")
    search_fields = ("client_name", "country", "testimonial_text")

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("email",)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "experience", "is_active", "order")
    list_filter = ("is_active", "position")
    search_fields = ("name", "bio", "expertise")
    ordering = ("order",)

