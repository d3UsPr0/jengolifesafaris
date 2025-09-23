from django.http import JsonResponse
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import QuotationForm
import json
from django.shortcuts import get_object_or_404, render
from .models import FAQ, BlogPost, Destination, SafariPackage, Testimonial
from django.core.mail import send_mail
from django.http import HttpResponse


def home(request):
    # Get all destinations or filter as needed
    destinations = Destination.objects.filter(is_popular=True)
    safari_packages = SafariPackage.objects.filter(is_featured=True)
    testimonials = Testimonial.objects.filter(is_featured=True).order_by('-created_at')[:3]
    faqs = FAQ.objects.filter(is_active=True).order_by('order', 'question')
    articles = BlogPost.objects.filter(
        is_published=True,
        published_date__lte=timezone.now()
    ).order_by('-published_date')
    
    context = {
        'destinations': destinations,
        'safari_packages': safari_packages,
        'testimonials': testimonials,
        'faqs': faqs,
        'articles': articles,
    }
    return render(request, 'web/home.html', context)

def destination(request, slug):
    # Get the destination by slug or return 404
    destination = get_object_or_404(Destination, slug=slug)

    # Get other destinations except current
    other_destinations = Destination.objects.exclude(id=destination.id)

    context = {
        'destination': destination,
        'other_destinations': other_destinations
    }
    return render(request, 'web/destination.html', context)


def destinations(request):
    # Get all destinations or filter as needed
    destinations = Destination.objects.filter(is_popular=True)  # or .all() for all destinations
    
    context = {
        'destinations': destinations
    }
    return render(request, 'web/destinations.html', context)



def safari(request, slug):
    # Get a single safari package detail
    safari_package = get_object_or_404(SafariPackage, slug=slug)
    itinerary_days = safari_package.itinerary_days.all()
    
    context = {
        'safari_package': safari_package,
        'itinerary_days': itinerary_days,
    }
    return render(request, 'web/safari.html', context)

def safaris(request):
    # List all safari packages
    safari_packages = SafariPackage.objects.all()
    
    context = {
        'safari_packages': safari_packages
    }
    return render(request, 'web/safaris.html', context)

def about(request):
    return render(request, 'web/about.html')

def articles(request):

    return render(request, 'web/articles.html')

def article(request, slug):
    # Get the article by slug or return 404
    article = get_object_or_404(BlogPost, slug=slug)

    context = {
        'article': article
    }
    return render(request, 'web/article.html', context)

def booking(request):
    return render(request, 'web/booking.html')

@csrf_exempt
@require_POST
def submit_quotation(request):
    try:
        # Parse JSON data from the request
        data = json.loads(request.body)
        print("Received form data:", data)  # Debug print
        
        form = QuotationForm(data)
        
        if form.is_valid():
            # Get form data
            form_data = form.cleaned_data
            print("Form is valid, cleaned data:", form_data)  # Debug print
            
            # Prepare email content
            subject = f"New Quotation Request from {form_data['name']}"
            
            # Render email template
            email_content = render_to_string('web/quotation_request.html', {
                'form_data': form_data,
                'site_name': 'Jengo Life Safaris'  # Use direct value for testing
            })
            
            # Get recipient emails from settings
            recipient_emails = [
    getattr(settings, 'CONTACT_EMAIL1', 'info@jengolifesafaris.com'),
    getattr(settings, 'CONTACT_EMAIL2', 'daudingusa1@gmail.com'),
]
            
            print("Attempting to send email to:", recipient_emails)  # Debug print
            
            # Try to send email
            try:
                email = EmailMessage(
                    subject=subject,
                    body=email_content,
                    from_email=settings.EMAIL_HOST_USER,
                    to=recipient_emails,
                    reply_to=[form_data['email']]
                )
                email.content_subtype = "html"
                email.send()
                print("Email sent successfully")  # Debug print
            except Exception as email_error:
                print("Email error:", str(email_error))  # Debug print
                return JsonResponse({
                    'success': False,
                    'message': f'Email sending failed: {str(email_error)}'
                })
            
            # Also try to send confirmation email
            try:
                user_subject = "Thank you for your quotation request"
                user_email_content = render_to_string('web/quotation_confirmation.html', {
                    'name': form_data['name'],
                    'site_name': 'Jengo Life Safaris'
                })
                
                user_email = EmailMessage(
                    subject=user_subject,
                    body=user_email_content,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[form_data['email']]
                )
                user_email.content_subtype = "html"
                user_email.send()
                print("Confirmation email sent successfully")  # Debug print
            except Exception as confirmation_error:
                print("Confirmation email error:", str(confirmation_error))  # Debug print
            
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your request! We will contact you shortly.'
            })
        else:
            print("Form errors:", form.errors)  # Debug print
            return JsonResponse({
                'success': False,
                'message': 'Please fill all required fields correctly.',
                'errors': form.errors
            })
            
    except Exception as e:
        print("General error:", str(e))  # Debug print
        return JsonResponse({
            'success': False,
            'message': f'An error occurred: {str(e)}'
        })
        
def test_email(request):
    try:
        send_mail(
            'Test Email from Django',
            'This is a test email to check if your settings are correct.',
            settings.EMAIL_HOST_USER,
            ['deuc60@gmail.com'],  # Your email
            fail_silently=False,
        )
        return HttpResponse("Test email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send test email: {str(e)}")
