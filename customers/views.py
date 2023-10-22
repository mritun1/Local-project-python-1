from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def product_news(request):
    return render(request,"customers/product_news.html")

def local_events(request):
    return render(request,"customers/local_events.html")

def local_market(request):
    return render(request,"customers/local_market.html")

def local_market_cat(request):
    return render(request,"customers/local_market_cat.html")

def local_business(request):
    return render(request,"customers/local_business.html")

def local_business_cat(request):
    return render(request,"customers/local_business_cat.html")

def local_people(request):
    return render(request,"customers/local_people.html")

def local_people_cat(request):
    return render(request,"customers/local_people_cat.html")

def my_posts(request):
    return render(request,"posts/my_posts.html")

def my_earnings(request):
    return render(request,"earnings/my_earnings.html")

def my_market(request):
    return render(request,"market/my_market.html")

def my_stores(request):
    return render(request,"stores/my_stores.html")

def delivery_boy(request):
    return render(request,"delivery/delivery_boy.html")

def my_referral(request):
    return render(request,"referral/my_referral.html")

def my_ads(request):
    return render(request,"advertisers/my_ads.html")

def my_analytics(request):
    return render(request,"analytics/my_analytics.html")

def my_saved(request):
    return render(request,"customers/my_saved.html")

def my_contacts(request):
    return render(request,"customers/my_contacts.html")

def my_business_contacts(request):
    return render(request,"customers/my_business_contacts.html")

def settings(request):
    return render(request,"customers/settings.html")

def local_offers(request):
    return render(request,"customers/local_offers.html")
