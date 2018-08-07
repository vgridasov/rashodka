from django.shortcuts import render
from .models import Ware
from django.core.paginator import Paginator


def index(request):
    ware_list = Ware.objects.all()
    paginator = Paginator(ware_list, 4)  # Кол-во записей на странице
    page = request.GET.get('page')
    wares = paginator.get_page(page)
    return render(request, 'wares/index.html', context={'wares': wares})