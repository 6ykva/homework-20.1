from django.core.management import BaseCommand

from homework.models import Category, Product


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()