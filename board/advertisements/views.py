from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

def advertisement_list(request, *args, **kwargs):
    transport = ['cruz 2011', 'focus 2009', 'rapid 2021']
    furniture = ['Тумба', 'Шкаф', 'Стол']
    toys = ['солдатик', 'машинка', 'мишка']
    return render(request, 'advertisements/advertisement_list.html', {'transport':transport, 'furniture':furniture, 'toys':toys})


def advertisement_detail(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_detail.html')


def courses_list(request, *args, **kwargs):
    return render(request, 'advertisements/courses_list.html')


def course_1(request, *args, **kwargs):
    return render(request, 'advertisements/course_1.html')


def course_2(request, *args, **kwargs):
    return render(request, 'advertisements/course_2.html')


def course_3(request, *args, **kwargs):
    return render(request, 'advertisements/course_3.html')


def course_4(request, *args, **kwargs):
    return render(request, 'advertisements/course_4.html')

req_count = 0
class Regions(View):
    
 
    def get(self, request):
        regions = ['Татарстан', 'Хакасия', 'Мари-Эл']  
        return render(request, 'advertisements/regions.html', {'regions':regions})
    def post(self, request):
        global req_count
        req_count = req_count + 1
        return HttpResponse(f'<h1>Регион создан, количество запросов { req_count } </h1>')


class Home(TemplateView):

    template_name = 'advertisements/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бесплатные объявления'
        context['description'] = 'Бесплатные объявления в вашем городе!'
        context['regions'] = ['Татарстан', 'Хакасия', 'Мари-Эл']
        context['categories'] = ['транспорт', 'недвижимость', 'услуги', 'электроника'] 
        return context

    def post(self, request, **kwargs):
        return HttpResponse(f'<h1>{ kwargs }</h1>')