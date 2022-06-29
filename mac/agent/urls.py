from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("layout",views.layout, name="layout"),
    path("plans",views.plans, name="plans"),
    path("login",views.login, name="login"),
    path("register",views.register, name="register"),
    path("forgot",views.forgot, name="forgot"),
    path("user_account",views.user_account, name="user_account"),
    path("logout",views.logout, name="logout"),
    path("ownsale",views.ownsale, name="ownsale"),
    path("ownrent",views.ownrent, name="ownrent"),
    path("displayrent/<int:rent_id>",views.displayrent, name="displayrent"),
    path("displaysale/<int:sale_id>",views.displaysale, name="displaysale"),
    path("payment",views.payment, name="payment"),
    path("office_index",views.office_index, name="office_index"),
    path("rent_edit/<int:rent_id>", views.rent_edit, name="rent_edit"),
    path("sale_edit/<int:sale_id>", views.sale_edit, name="sale_edit"),
    path("office_layout",views.office_layout, name="office_layout"),
    path("office_login",views.office_login, name="office_login"),
    path("office_logout",views.office_logout, name="office_logout"),
    path("office_rentdb",views.office_rentdb, name="office_rentdb"),
    path("office_view",views.office_view, name="office_view"),
    path("office_saleblock",views.office_saleblock, name="office_saleblock"),
    path("office_rentblock",views.office_rentblock, name="office_rentblock"),
    path("ssent",views.ssent, name="ssent"),
    path("search",views.search, name="search"),

]