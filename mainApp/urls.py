from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.test, name= "test_func"),
    path('sendMail/', views.send_mail_to_all, name= "send_mail_to_all"),
]