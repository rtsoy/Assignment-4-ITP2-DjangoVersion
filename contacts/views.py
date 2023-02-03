from django.shortcuts import render, redirect
from django.views.generic.base import View

from .models import Contact


class ContactView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, 'main.html', {'contacts': contacts})


class AddContact(View):
    def get(self, request):
        return render(request, 'add-contact.html')

    def post(self, request):
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        Contact.objects.create(name=name, phone_number=phone_number, email=email)
        return redirect('/')


class EditContact(View):
    def get(self, request, id):
        contact = Contact.objects.get(id=f'{id}')
        return render(request, 'edit-contact.html', {'contact': contact})

    def post(self, request, id):
        contact = Contact.objects.get(id=f'{id}')
        contact.name = request.POST['name']
        contact.phone_number = request.POST['phone_number']
        contact.email = request.POST['email']
        contact.save()
        return redirect('/')


class DeleteContact(View):
    def get(self, request, id):
        Contact.objects.get(id=f'{id}').delete()
        return redirect('/')
