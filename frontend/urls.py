from django.urls import path
from frontend import views

urlpatterns=[
    path('indexpg/',views.indexpg,name="indexpg"),
    path('gallerypg/',views.gallerypg,name="gallerypg"),
    path('aboutpg/',views.aboutpg,name="aboutpg"),
    path('pricingpg/',views.pricingpg,name="pricingpg"),
    path('bookingpg/',views.bookingpg,name="bookingpg"),
    path('contactpg/',views.contactpg,name="contactpg"),
    path('loginpg/', views.loginpg, name="loginpg"),
    path('saveloginpg/', views.saveloginpg, name="saveloginpg"),
    path('custemerlogin/', views.custemerlogin, name="custemerlogin"),
    path('userlogout/', views.userlogout, name="userlogout")


]