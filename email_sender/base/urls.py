from django.urls import path
from . import views

urlpatterns = [
    path("", views.from_given_email, name='from_given_email'),
    # path("email_query/", views.email_query, name='email_query'),
    path("excel/", views.from_excel, name='from_excel'),
    path("string/", views.from_string, name='from_string'),
]