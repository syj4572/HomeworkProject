from django.urls import path
from . import views

urlpatterns = [
    path("rr/", views.rr, name="rrname"),
    path("cc/", views.cc, name="ccname"),
    path("uu/", views.uu, name="uuname"),
    path("dd/", views.dd, name="ddname"),
    # path("update_cnt/", views.update_cnt, name="update_cnt"),
]