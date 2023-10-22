from django.urls import path

from customers import views


urlpatterns = [
    path('',views.index,name="index"),
    path('local-offers/',views.local_offers,name="local_offers"),
    path('product-news/',views.product_news,name="product_news"),
    path('local-events/',views.local_events,name="local_events"),
    path('local-market/',views.local_market,name="local_market"),
    path('local-market-cat/',views.local_market_cat,name="local_market_cat"),
    path('local-business/',views.local_business,name="local_business"),
    path('local-business-cat/',views.local_business_cat,name="local_business_cat"),
    path('local-people/',views.local_people,name="local_people"),
    path('local-people-cat/',views.local_people_cat,name="local_people_cat"),
    path('my-posts/',views.my_posts,name="my_posts"),
    path('my-earnings/',views.my_earnings,name="my_earnings"),
    path('my-market/',views.my_market,name="my_market"),
    path('my-stores/',views.my_stores,name="my_stores"),
    path('delivery-boy/',views.delivery_boy,name="delivery_boy"),
    path('my-referral/',views.my_referral,name="my_referral"),
    path('my-advertisement/',views.my_ads,name="my_ads"),
    path('my-analytics/',views.my_analytics,name="my_analytics"),
    path('my-saved/',views.my_saved,name="my_saved"),
    path('my-contacts/',views.my_contacts,name="my_contacts"),
    path('my-business-contacts/',views.my_business_contacts,name="my_business_contacts"),
    path('settings/',views.settings,name="settings"),
]