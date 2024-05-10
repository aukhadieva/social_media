from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailing.forms import ClientForm
from mailing.models import Client
from utils import TitleMixin


class ClientCreateView(TitleMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')
    title = 'Создание клиента'


class ClientListView(TitleMixin, ListView):
    model = Client
    title = 'Список клиентов'


class ClientDetailView(TitleMixin, DetailView):
    model = Client

    def get_title(self):
        return self.object.full_name


class ClientDeleteView(TitleMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')
    title = 'Удаление клиента'


class ClientUpdateView(TitleMixin, UpdateView):
    model = Client
    form_class = ClientForm
    title = 'Редактирование клиента'

    def get_success_url(self):
        client = self.get_object()
        return reverse('mailing:view_client', args=[client.pk])
