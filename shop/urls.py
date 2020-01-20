from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about",views.about,name="AboutUs"),
    path("contact",views.contact,name="ContatUs"),
    path("product/<int:myid>",views.productView,name="ProductView"),
    path("register",views.register,name="Register"),
    path("cart",views.checkout,name="Checkout"),
    path("login",views.login,name="Login"),
    path("logout",views.logout,name="Logout")
]