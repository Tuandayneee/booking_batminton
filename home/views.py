from django.shortcuts import render, redirect
from partner.models import BadmintonCenter
from django.db.models import Min

def home(request):
    if request.user.is_authenticated:
        if request.user.role == 'partner':
            return redirect('partner_dashboard')
        elif request.user.role == 'staff':
            return redirect('pos_sales')
    
    centers = BadmintonCenter.objects.annotate(
        min_price=Min('courts__base_price_per_hour') 
    )
   
    return render(request ,'home/home.html', {'centers': centers, })

def partner_info(request):
    return render(request, 'home/partner_info.html')

def about_page(request):
    return render(request, 'home/about.html')

def terms_page(request):
    return render(request, 'home/terms.html')

def privacy_page(request):
    return render(request, 'home/privacy.html')

def booking_guide(request):
    return render(request, 'home/booking_guide.html')

def contact_partner(request):
    return render(request, 'home/contact_partner.html')

def faq(request):
    return render(request, 'home/faq.html')
