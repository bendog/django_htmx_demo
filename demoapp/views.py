from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse_lazy
from django.views import generic

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = Contact
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
        }


class ContactIndex(generic.TemplateView):
    template_name = "demoapp/contact_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Contact.objects.all()
        context["form"] = ContactForm
        return context


def create_contact(request):
    if not request.method == "POST":
        raise HttpResponseNotAllowed
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return render(
            request, "demoapp/contact_list.html", {"object_list": Contact.objects.all()}
        )
    raise HttpResponseBadRequest


class ContactList(generic.ListView):
    model = Contact
