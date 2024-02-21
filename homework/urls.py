from django.urls import path

from homework.apps import HomeworkConfig
from homework.views import index, category_product

app_name = HomeworkConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/products/', category_product, name='category_product')

]
