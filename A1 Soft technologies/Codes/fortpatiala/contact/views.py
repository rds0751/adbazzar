# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'

    def get_success_url(self):
        return reverse('contact:contact')

    def form_valid(self, form):
        model = Contact()

        model.name = form.cleaned_data['name']
        model.email = form.cleaned_data['email']
        model.subject = form.cleaned_data['subject']
        model.message = form.cleaned_data['message']
        model.save()
        if form.send_email():
            messages.info(self.request, 'Thank you for your message. We will be in touch shortly.')
        else:
            messages.error(self.request, "We couldn't send your message. Please try again later.")
        return super(ContactView, self).form_valid(form)