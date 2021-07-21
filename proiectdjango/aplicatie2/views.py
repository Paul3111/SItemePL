from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse
from aplicatie2.models import Companies

class CreateLocationView(CreateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:adauga')


class ListLocationView(ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'


class UpdateLocationView(UpdateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:listare')