from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name="index"),
    path("index2",views.index2,name="index2"),
    path("about",views.about,name="about"),
    path("blog",views.blog,name="blog"),
    path("blog_single",views.blog_single,name="blog_single"),
    path("menu",views.menu,name="menu"),
    path("booking",views.booking,name="booking"),
    path("contact",views.contact,name="contact"),
    path("gal",views.gallery,name="gallery"),
    path("addtocart",views.addtocart,name="addtocart"),
    path("confirmation",views.confirmation, name="confirmation"),
    path("terms",views.term,name="terms"),
    path("policy",views.policy,name="policy"),
    path("Service/<int:cid>",views.Service,name="Service"),
    path("serve",views.serve,name="serve"),
    path("search",views.search,name="search"),  
    path("dashboard",views.dashboard,name="dashboard"),
    path("addser",views.addser,name="addser"),
    path("remove_product",views.remove_product,name="remove_product"),
    
]
 