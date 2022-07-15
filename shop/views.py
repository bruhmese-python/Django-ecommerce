
from django.shortcuts import get_object_or_404, render
from matplotlib.style import available
from requests import request
from .models import categ, product
from cart.models import cartlist
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.


def home(requests, c_slug=None):
    prodt = None
    c_page = None
    if(c_slug != None):
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = product.objects.filter(category=c_page, available=True)
    else:
        prodt = product.objects.all().filter(available=True)
    ct = categ.objects.all()
    paginator = Paginator(prodt, 4)
    try:
        page = int(requests.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)

    return render(requests, R"Modified_files\index.html", {'pr': prodt, 'ct': ct, 'pg': pro})


def item(requests, c_slug=None, i_slug=None):
    try:
        item = product.objects.get(slug=i_slug)
    except Exception as e:
        raise e
    return render(requests, R"Modified_files\item.html", {'item': item})


def login(requests):
    return render(requests, R"Modified_files\Login.html")


def register(requests):
    return render(requests, R"Modified_files\Register.html")


def searching(request):
    if 'query' in request.GET:
        query = request.GET.get('query')
        prod = product.objects.all().filter(
            Q(name__contains=query) | Q(desc__contains=query))
    return render(request, R"Modified_files\Search.html", {'qr': query, 'pr': prod})


def cart(requests):
    items = cart
    return render(requests, R"Modified_files\Cart.html")


def base(requests):
    return render(requests, R"Modified_files\base.html")
