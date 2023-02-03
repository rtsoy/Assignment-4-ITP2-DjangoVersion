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
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        Contact.objects.create(**data)
        return redirect('/')


class EditContact(View):
    def get(self, request, id):
        contact = Contact.objects.get(id=id)
        return render(request, 'edit-contact.html', {'contact': contact})

    def post(self, request, id):
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        Contact.objects.filter(id=id).update(**data)
        return redirect('/')


class DeleteContact(View):
    def get(self, request, id):
        Contact.objects.get(id=f'{id}').delete()
        return redirect('/')
