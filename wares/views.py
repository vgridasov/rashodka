from django.shortcuts import render, get_object_or_404
from .models import Ware
from django.core.paginator import Paginator


def index(request):
    ware_list = Ware.objects.all()
    paginator = Paginator(ware_list, 6)  # Кол-во записей на странице
    page = request.GET.get('page')
    wares = paginator.get_page(page)
    return render(request, 'wares/index.html', context={'wares': wares})


def ware_detail(request, ware_id):
    ware = get_object_or_404(Ware, pk=ware_id)
    return render(request, 'wares/ware_detail.html', context={'ware': ware})
