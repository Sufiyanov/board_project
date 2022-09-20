from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class About(TemplateView):
    template_name = 'info/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бесплатные объявления'
        context['description'] = 'Бесплатные объявления в вашем городе!'
        return context

class Contacts(TemplateView):
    template_name = 'info/contacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = '89600340075'
        context['mail'] = 'srkt@mail.ru'
        return context


def categories(request, *args, **kwargs):
    categories = ['транспорт', 'недвижимость', 'услуги', 'электроника']
    return render(request, 'info/categories.html', {'categories': categories})


def regions(request, *args, **kwargs):
    regions = ['Татарстан', 'Хакасия', 'Мари-Эл']
    return render(request, 'info/regions.html', {'regions': regions})