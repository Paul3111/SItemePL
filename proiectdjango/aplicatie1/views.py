from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse
from aplicatie1.models import Location
# Create your views here.

class CreateLocationView(CreateView):
    model = Location
    fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:adauga')


class ListLocationView(ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'


class UpdateLocationView(UpdateView):
    model = Location
    fields = '__all__'
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:listare')
