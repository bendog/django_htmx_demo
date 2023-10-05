from django.urls import path

from . import views

app_name = "demoapp"
urlpatterns = [
    path("", views.ContactIndex.as_view(), name="contact-index"),
    path("list/", views.ContactList.as_view(), name="contact-list"),
    path("create/", views.create_contact, name="contact-create"),
]
