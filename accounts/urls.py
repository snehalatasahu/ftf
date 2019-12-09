from django.urls import path
from . import views

urlpatterns = [
    path("sign-up", views.sign_up, name="sign-up"),
    path("log-in", views.log_in, name="log-in"),
    path("log-out", views.log_out, name="log-out"),

]