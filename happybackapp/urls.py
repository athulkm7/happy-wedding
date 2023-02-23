from django.urls import path
from happybackapp import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addadmin/', views.addadmin, name="addadmin"),
    path('saveadminpage/',views.saveadminpage,name="saveadminpage"),
    path('displayadmin/',views.displayadmin,name="displayadmin"),
    path('editadmin/<int:dataid>/',views.editadmin,name="editadmin"),
    path('updateadmin/<int:dataid>',views.updateadmin,name="updateadmin"),
    path('deleteadmin/<int:dataid>',views.deleteadmin,name="deleteadmin"),

    path('gallery/', views.gallery, name="gallery"),
    path('savegallery/', views.savegallery, name="savegallery"),
    path('displaygallery/',views.displaygallery,name="displaygallery"),
    path('editgallery/<int:dataid>/',views.editgallery,name="editgallery"),
    path('updategallery/<int:dataid>',views.updategallery,name="updategallery"),
    path('deletegallery/<int:dataid>',views.deletegallery,name="deletegallery"),

    path('pricing/', views.pricing, name="pricing"),
    path('savepricing/', views.savepricing, name="savepricing"),
    path('displaypricing/', views.displaypricing, name="displaypricing"),
    path('editpricing/<int:dataid>/', views.editpricing, name="editpricing"),
    path('updatepricing/<int:dataid>', views.updatepricing, name="updatepricing"),
    path('deletepricing/<int:dataid>', views.deletepricing, name="deletepricing"),

    path('viewbooking/', views.viewbooking, name="viewbooking"),
    path('deletebooking/<int:dataid>', views.deletebooking, name="deletebooking"),

    path('viewcontact/', views.viewcontact, name="viewcontact"),
    path('deletecontact/<int:dataid>', views.deletecontact, name="deletecontact"),

    path('loginpage/',views.loginpage, name="loginpage"),
    path('adminloginpage/',views.adminloginpage, name="adminloginpage")


]

