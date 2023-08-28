from pydoc import pager
from turtle import xcor
from django.shortcuts import render
from django.views.generic import ListView
from .models import Cars
from math import ceil


def page_objects(request):

    if request.method == 'POST':
        page = request.POST['Page']
        from_number = int(page)*3 - 2
        to_number = int(page)*3
        print(from_number, to_number)
        data = Cars.objects.filter(id__range=(from_number, to_number))
        view_count = Cars.objects.count()
        context = {
            'data': data,
            'page_len': ceil(view_count / 3),
            'curr_page': page
            }
        return render(request, 'home.html', context)
    return render(request, 'home.html')