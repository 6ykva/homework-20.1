from django.shortcuts import render

from homework.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Магазин запчастей',
    }
    return render(request, 'homework/index.html', context)


def category_product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Категория фильтров  - {category_item.name.title()}',
    }
    return render(request, 'homework/products.html', context)
